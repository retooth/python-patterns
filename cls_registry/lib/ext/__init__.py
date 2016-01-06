from ..classreg import ClassRegistry
from os import path, listdir
ext_classes = ClassRegistry()

# Find out the path this file resides in
abs_file = path.abspath(__file__)
abs_dir = path.dirname(abs_file)

# list files
files_in_ext_path = listdir(abs_dir)

ext_modules = []
for fn in files_in_ext_path:
    # filter python files
    if fn.endswith('.py') and not fn == '__init__.py':
        # translate them into module syntax
        # and import
        mod_rel = fn[0:-3]
        __import__(mod_rel, globals=globals())

