from lib.ext import ext_classes

print(ext_classes)

foo_cls = ext_classes.get('foo_extension_cls')
f = foo_cls()
f.baz()
