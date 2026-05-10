from app_name import config
from app_name.package_1 import module_A


def run(args):
    module_A.some_function()
    print(config.SOME_SETTING)
