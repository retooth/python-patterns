from . import ext_classes

# register Foo in the ext_classes registry
# with its class_entry decorator


@ext_classes.class_entry(registry_key='foo_extension_cls')
class Foo(object):

    def baz(self):
        print("baz!!")
