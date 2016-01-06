class ClassRegistry(dict):

    def class_entry (self, registry_key=None):

        """ decorator factory to insert classes into
        this registry """

        def _inner (cls_):

            # _registry_key assignment is a workaround
            # for the missing nonlocal statement in python2.x

            if registry_key is None:
                _registry_key = cls_.__name__
            else:
                _registry_key = registry_key

            self[_registry_key] = cls_
            return cls_

        return _inner
