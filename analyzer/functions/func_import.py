def dyn_import_cls(module_name, class_name):
    """
    :param module_name: module from which to import the class
    :param class_name: name of the class
    :return: class
    """
    module = __import__(module_name)        # import module
    my_class = getattr(module, class_name)  # create class
    return my_class
