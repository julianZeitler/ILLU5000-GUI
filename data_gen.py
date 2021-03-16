import numpy as np
from scipy.io import savemat

phi = np.linspace(0.1, 37.1, 1000)
sinus = np.sin(phi)

dic = {'plot_data': {'data': {'phi': {'values': phi, 'name': 'x_data', 'unit': 'rad'},
                              'sinus': {'values': sinus, 'name': 'y_data', 'unit': 'm'}},
                     'meta': {'timestamp_last_sample': 123,
                              'location': 'Deutschland, Oberkochen',
                              'machine': 'some machine',
                              'worker': 'Max Mustermann'},
                     'plot': {'trig': {'figure': [{'subplot': [{'plots': [['phi', 'sinus']]}]}]}}}}

savemat('data.mat', dic)
