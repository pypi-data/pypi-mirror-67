# copyright (c) 2020 PaddlePaddle Authors. All Rights Reserve.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import yaml
import os.path as osp
import six
import copy
from collections import OrderedDict
import paddle.fluid as fluid
from paddle.fluid.framework import Parameter
import paddlex
import paddlex.utils.logging as logging


def load_model(model_dir):
    if not osp.exists(osp.join(model_dir, "model.yml")):
        raise Exception("There's not model.yml in {}".format(model_dir))
    with open(osp.join(model_dir, "model.yml")) as f:
        info = yaml.load(f.read(), Loader=yaml.Loader)
    status = info['status']

    if not hasattr(paddlex.cv.models, info['Model']):
        raise Exception("There's no attribute {} in paddlex.cv.models".format(
            info['Model']))

    if info['_Attributes']['model_type'] == 'classifier':
        model = paddlex.cv.models.BaseClassifier(**info['_init_params'])
    else:
        model = getattr(paddlex.cv.models,
                        info['Model'])(**info['_init_params'])
    if status == "Normal" or \
            status == "Prune":
        startup_prog = fluid.Program()
        model.test_prog = fluid.Program()
        with fluid.program_guard(model.test_prog, startup_prog):
            with fluid.unique_name.guard():
                model.test_inputs, model.test_outputs = model.build_net(
                    mode='test')
        model.test_prog = model.test_prog.clone(for_test=True)
        model.exe.run(startup_prog)
        if status == "Prune":
            from .slim.prune import update_program
            model.test_prog = update_program(model.test_prog, model_dir,
                                             model.places[0])
        import pickle
        with open(osp.join(model_dir, 'model.pdparams'), 'rb') as f:
            load_dict = pickle.load(f)
        fluid.io.set_program_state(model.test_prog, load_dict)

    elif status == "Infer" or \
            status == "Quant":
        [prog, input_names, outputs] = fluid.io.load_inference_model(
            model_dir, model.exe, params_filename='__params__')
        model.test_prog = prog
        test_outputs_info = info['_ModelInputsOutputs']['test_outputs']
        model.test_inputs = OrderedDict()
        model.test_outputs = OrderedDict()
        for name in input_names:
            model.test_inputs[name] = model.test_prog.global_block().var(name)
        for i, out in enumerate(outputs):
            var_desc = test_outputs_info[i]
            model.test_outputs[var_desc[0]] = out
    if 'Transforms' in info:
        transforms_mode = info.get('TransformsMode', 'RGB')
        if transforms_mode == 'RGB':
            to_rgb = True
        else:
            to_rgb = False
        model.test_transforms = build_transforms(model.model_type,
                                                 info['Transforms'], to_rgb)
        model.eval_transforms = copy.deepcopy(model.test_transforms)

    if '_Attributes' in info:
        for k, v in info['_Attributes'].items():
            if k in model.__dict__:
                model.__dict__[k] = v

    logging.info("Model[{}] loaded.".format(info['Model']))
    return model


def build_transforms(model_type, transforms_info, to_rgb=True):
    if model_type == "classifier":
        import paddlex.cv.transforms.cls_transforms as T
    elif model_type == "detector":
        import paddlex.cv.transforms.det_transforms as T
    elif model_type == "segmenter":
        import paddlex.cv.transforms.seg_transforms as T
    transforms = list()
    for op_info in transforms_info:
        op_name = list(op_info.keys())[0]
        op_attr = op_info[op_name]
        if not hasattr(T, op_name):
            raise Exception(
                "There's no operator named '{}' in transforms of {}".format(
                    op_name, model_type))
        transforms.append(getattr(T, op_name)(**op_attr))
    eval_transforms = T.Compose(transforms)
    eval_transforms.to_rgb = to_rgb
    return eval_transforms
