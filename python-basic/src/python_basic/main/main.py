import sys
from python_basic.package_1 import module_A
from . import settings

def main(args):
    module_A.some_function()
    print('main')
    print(settings.SOME_SETTING)