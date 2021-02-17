def dyn_import_obj(module_name, class_name, *args, **kwargs):
    module = __import__(module_name)
    my_class = getattr(module, class_name)
    obj = my_class(*args, **kwargs)
    return obj


def dyn_import_cls(module_name, class_name):
    module = __import__(module_name)
    my_class = getattr(module, class_name)
    return my_class
