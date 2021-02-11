import scipy.io as spio
from numpy import ndarray

# source https://stackoverflow.com/questions/7008608/scipy-io-loadmat-nested-structures-i-e-dictionaries


def loadmat(filename):
    # this function should be called instead of direct spio.loadmat
    # as it cures the problem of not properly recovering python dictionaries
    # from mat files. It calls the function check keys to cure all entries
    # which are still mat-objects
    data = spio.loadmat(filename, struct_as_record=False, squeeze_me=True)

    def _check_keys(dict):
        # checks if entries in dictionary are mat-objects. If yes
        # todict is called to change them to nested dictionaries
        for key in dict:
            if isinstance(dict[key], spio.matlab.mio5_params.mat_struct):
                dict[key] = _todict(dict[key])
        return dict

    def _todict(matobj):
        # A recursive function which constructs from matobjects nested dictionaries
        dic = {}
        for strg in matobj._fieldnames:
            elem = matobj.__dict__[strg]
            if isinstance(elem, spio.matlab.mio5_params.mat_struct):
                dic[strg] = _todict(elem)
            elif isinstance(elem, ndarray):
                dic[strg] = _tolist(elem)
            else:
                dic[strg] = elem
        return dic

    def _tolist(array):
        elem_list = []
        for elem in array:
            if isinstance(elem, spio.matlab.mio5_params.mat_struct):
                elem_list.append(_todict(elem))
            elif isinstance(elem, ndarray):
                elem_list.append(_tolist(elem))
            else:
                elem_list.append(elem)
        return elem_list

    return _check_keys(data)
