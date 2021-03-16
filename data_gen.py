import numpy as np
from scipy.io import savemat

phi = np.linspace(0, 37, 1000)
sinus = np.sin(phi)

dic = {'plot_data': {'data': {'phi': {'values': phi, 'name': 'phi', 'unit': 'rad'},
                              'sinus': {'values': sinus, 'name': 'sinus', 'unit': 'm'}},
                     'meta': {'timestamp_last_sample': 123,
                              'location': 'Deutschland, Oberkochen',
                              'machine': 'some machine',
                              'worker': 'Max Mustermann'},
                     'plot': {'trig': {'figure': [{'subplot': [{'plots': [['phi', 'sinus']]}]}]}}}}

savemat('data.mat', dic)
