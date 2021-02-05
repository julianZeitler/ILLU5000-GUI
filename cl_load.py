import scipy.io as spio
import numpy as np

# source https://stackoverflow.com/questions/7008608/scipy-io-loadmat-nested-structures-i-e-dictionaries


class LoadMat:
    def __init__(self, filename):
        self.filename = filename
        self

    def loadmat(self):
        data = spio.loadmat(self.filename, struct_as_record=False, squeeze_me=True)
        return self._check_keys(data)

    def _check_keys(self, data):
        #checks if entries in dictionary are mat-objects. If yes
        #todict is called to change them to nested dictionaries
        for key in data:
            if isinstance(data[key], spio.matlab.mio5_params.mat_struct):
                data[key] = self._todict(data[key])
        return data

    def _todict(self, matobj):
        #A recursive function which constructs from matobjects nested dictionaries
        dic = {}
        for strg in matobj._fieldnames:
            elem = matobj.__dict__[strg]
            if isinstance(elem, spio.matlab.mio5_params.mat_struct):
                dic[strg] = self._todict(elem)
            else:
                dic[strg] = elem
        return dic


