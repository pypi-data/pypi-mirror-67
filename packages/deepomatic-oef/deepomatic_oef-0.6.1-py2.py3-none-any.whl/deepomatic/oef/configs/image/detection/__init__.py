from . import rcnn
from . import ssd
from . import yolo

modules = [rcnn, ssd, yolo]

config_items = []
for m in modules:
    config_items += list(m.configs.items())

configs = dict(config_items)

assert len(configs) == len(config_items)
