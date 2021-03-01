from importlib import import_module


def dyn_import_cls(module_name, class_name):
    """
    This function can be used to import classes dynamically.
    The return can be used like any other class.
    The function is used to dynamically import plot types specified in plot_types package.
    :param module_name: module from which to import the class
    :param class_name: name of the class
    :return: class
    """
    module = import_module(module_name)        # import module
    my_class = getattr(module, class_name)  # create class
    return my_class
