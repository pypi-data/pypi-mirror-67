import os
import json
import copy
import logging

from deepomatic.oef.configs.model_args import ModelArguments
from deepomatic.oef.configs.image.backbones import backbones
from deepomatic.oef.configs.image import configs

from deepomatic.oef.configs.utils import dict_inject

logger = logging.getLogger(__name__)

###############################################################################

DEFAULT_LEARNING_RATE_POLICY = {
    "manual_step_learning_rate": {
        "schedule": [
            {
                "learning_rate_factor": 0.1,
                "step_pct": 0.33
            },
            {
                "learning_rate_factor": 0.01,
                "step_pct": 0.66
            }
        ],
    }
}

DEFAULT_OPTIMIZER = {
    "momentum_optimizer": {
    },
}

# DEFAULT_OPTIMIZER = {
#     "rms_prop_optimizer": {
#     },
#     "use_moving_average": True
# }


###############################################################################

class ModelFamilies:
    def __init__(self):
        self._families = {}

    def add_family(self, family_name):
        f = ModelFamily(family_name)
        self._families[family_name] = f
        return f

    def dump(self, module_path=None):
        dumped_groups = {}
        for _, family in self._families.items():
            for key, model_args in family.to_dict().items():
                key_parts = key.split('.')
                group_name = ' - '.join([key_parts[0], key_parts[1]]).upper()
                if group_name not in dumped_groups:
                    dumped_groups[group_name] = {}
                dumped_groups[group_name][key] = model_args
        dumped_groups = list(dumped_groups.items())
        dumped_groups.sort()
        dumped_groups = ''.join([self._dump_group_(group_name, group) for group_name, group in dumped_groups])
        dumped_txt = """# This file has been generated with `make models`: DO NOT EDIT!
from deepomatic.oef.configs.model_args import ModelArguments

model_list = {\n""" + dumped_groups + "}\n"  # add trailing line
        dumped_txt = dumped_txt.replace('"@', '').replace('@"', '').replace('\\"', '"')

        if module_path is None:
            module_path = os.path.join(os.path.dirname(__file__), 'model_list.py')
        with open(module_path, 'w') as f:
            f.write(dumped_txt)

    def _dump_group_(self, group_name, group):
        txt = json.dumps(group, sort_keys=True, indent=4, separators=(',', ': '))
        lines = txt.split('\n')
        lines[0] = '    # ' + group_name
        lines[-2] += ','
        lines[-1] = '\n'
        return '\n'.join(lines)


class ModelFamily:

    def __init__(self, family_name):
        self._family_name = family_name
        self._models = {
        }

    @property
    def name(self):
        return self._family_name

    def to_dict(self):
        return {key: repr(model) for key, model in self._models.items()}

    def add_model(self, key, display_name, default_args, pretraining_none=None, pretraining_natural_rgb=None):
        if pretraining_none is None:
            self._add_model_('pretraining_none', key, display_name, default_args)
        else:
            self._add_model_with_pretrained_weights_(
                'pretraining_none',
                key, display_name, default_args,
                pretraining_none)

        if pretraining_natural_rgb is not None:
            self._add_model_with_pretrained_weights_(
                'pretraining_natural_rgb',
                key, display_name, default_args,
                pretraining_natural_rgb)

    def _add_model_with_pretrained_weights_(self, pretraining_type, key, display_name, default_args, pretrained_weights):
        default_args = dict_inject(copy.deepcopy(default_args), {
            'trainer': {
                'pretrained_parameters': pretrained_weights
            },
        })
        self._add_model_(pretraining_type, key, display_name, default_args)

    def _add_model_(self, pretraining_type, key, display_name, default_args):
        model_key = '{}.{}.{}'.format(self._family_name, pretraining_type, key)
        self._models[model_key] = ModelArguments(display_name, default_args)


###############################################################################

# Script to add a model family
common_default_args = {
    'trainer': {
        'learning_rate_policy': DEFAULT_LEARNING_RATE_POLICY,
        'optimizer': DEFAULT_OPTIMIZER
    }
}

def add_models_to_family(family, model_type_key, model_type_config):
    meta_arch = None
    if model_type_config['model_meta_arch'] is not None:
        meta_arch = model_type_config['model_meta_arch']

    def update_args(args, new_args):
        nonlocal meta_arch
        return dict_inject(args, new_args, shortcuts={
            '@model': ['trainer', family.name],
            '@meta_arch': ['trainer', family.name, meta_arch],
        })

    print('Generating {}.{}.*'.format(family.name, model_type_key))

    default_args = {}
    default_args = update_args(default_args, common_default_args)
    if meta_arch is not None:
        # IMPORTANT: This sets the meta_arch one-of even if it has not field
        default_args = update_args(default_args, {'@model.{}'.format(meta_arch): {}})
    default_args = update_args(default_args, model_type_config['model_default_args'])
    model_type_name = model_type_config['display_name']

    for backbone_key, backbone_args in model_type_config['backbones'].items():
        meta_arch_full_key = '{}.{}'.format(model_type_key, backbone_key)
        print('Generating {}.{}:'.format(family.name, meta_arch_full_key))
        # Select pretrained weights. Putting None as a pretrained weight selects the one of the backbone
        backbone = backbones[backbone_key]
        pretrained_parameters = {}
        for pretraining_key, backbone_list in model_type_config['pretrained_parameters'].items():
            if backbone_key in backbone_list:
                path = backbone_list[backbone_key]
                if path is None:
                    if 'pretrained_parameters' in backbone and pretraining_key in backbone['pretrained_parameters']:
                        path = backbone['pretrained_parameters'][pretraining_key]
                    else:
                        logger.error("Cannot find the pretrained_parameters.{} for '{}'. Refered in {}.{}".format(pretraining_key, backbone_key, model_type_key, backbone_key))
                if path is not None:  # if path is None: we could not find the actual path and we logged an error just above
                    pretrained_parameters['pretraining_' + pretraining_key] = path

        args = update_args(default_args, {'@model.backbone': backbone['backbone_args']})  # default backbone args
        args = update_args(args, backbone_args)  # backbone args according to the meta-arch
        family.add_model(
            meta_arch_full_key,
            '{} - {}'.format(model_type_name, backbone['display_name']),
            args,
            **pretrained_parameters
        )


###############################################################################

families = ModelFamilies()

for family_name, family_config in configs.items():
    family = families.add_family(family_name)
    for model_type_key, model_type_config in family_config.items():
        add_models_to_family(
            family,
            model_type_key,
            model_type_config)


###############################################################################

def generate(module_path=None):
    families.dump(module_path)


if __name__ == '__main__':
    generate()
