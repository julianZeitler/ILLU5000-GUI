from dataclasses import is_dataclass, asdict
from copy import deepcopy

from numpy import ndarray
from scipy.io import loadmat, savemat
from scipy.io.matlab.mio5_params import mat_struct

'''
func_mat.py contains the function load and save.
load loads a matlab file and outputs structs as a python dictionary and vectors as python lists
save writes the cl_data object to a dictionary, which can then be written to a matlab file
'''


def inner_classes(obj):
    """
    :param obj: Class instance
    :return: A list of class instances, that were instanciated by a class inside of the class obj originated from
    """
    return [cls_attribute for cls_attribute in obj.__dict__.values() if 'object' in str(cls_attribute)]


def save(object, file: str = None, names=['PlotData']):
    """ Save is a recursive function, which goes over the hole data structure (cl_data)
        and converts it back to a dictionary
    :param object: The object, which should be converted
    :param names: [typically: 'PlotData'] The names of the inner classes, required for the next recursion step
    :param file: Default: None. If specified, save writes the dictionary to .mat file with the name specified in file
    :return: Returns a dictionary
    """

    # Python passes arguments by assignment, so the original object would be changed
    instance = deepcopy(object)

    # vars() returns __dict__ attribute of an object
    # --> extracts the objects variables as a dictionary
    dic = vars(instance)

    for key, val in dic.items():
        # if the name of val is in names, following code gets executed:
        # val.__class__.__name__ returns the name of the class val was created from
        if str(val.__class__.__name__) in names:
            names = inner_classes(val)
            dic[key] = save(val, names=names)

        # handle dictionaries
        elif isinstance(val, dict):
            for k, v in val.items():
                names = inner_classes(v)
                dic[key][k] = save(v, names=names)

        # handle lists
        elif isinstance(val, list):
            for i in range(len(val)):
                try:
                    names = inner_classes(val[i])
                    val[i] = save(val[i], names=names)
                except: pass

        elif is_dataclass(val):
            dic[key] = asdict(val)

    if file:
        savemat(file, dic)
    return dic


def load(filename):
    """
    source https://stackoverflow.com/questions/7008608/scipy-io-loadmat-nested-structures-i-e-dictionaries
    this function should be called instead of direct scipy.io.loadmat
    as it cures the problem of not properly recovering python dictionaries
    from mat files. It calls the function check keys to cure all entries
    which are still mat-objects

    :param filename: Name of matlab file
    :return: Dictionary of the matlab data structure
    """
    data = loadmat(filename, struct_as_record=False, squeeze_me=True)

    def _check_keys(dic):
        # checks if entries in dictionary are mat-objects. If yes
        # todict is called to change them to nested dictionaries
        for key in dic:
            if isinstance(dic[key], mat_struct):
                dic[key] = _todict(dic[key])
        return dic

    def _todict(matobj):
        # A recursive function which constructs from matobjects nested dictionaries
        dic = {}
        for strg in matobj._fieldnames:
            elem = matobj.__dict__[strg]
            if isinstance(elem, mat_struct):
                dic[strg] = _todict(elem)
            elif isinstance(elem, ndarray):
                dic[strg] = _tolist(elem)
            else:
                dic[strg] = elem
        return dic

    def _tolist(array):
        # convert numpy arrays from the matobj to python lists
        elem_list = []
        for elem in array:
            if isinstance(elem, mat_struct):
                elem_list.append(_todict(elem))
            elif isinstance(elem, ndarray):
                elem_list.append(_tolist(elem))
            else:
                elem_list.append(elem)
        return elem_list

    return _check_keys(data)
