import numpy as np
from scipy.io import savemat

xdata = np.linspace(0.1, 37.1, 1000)
ydata = np.sin(xdata)

dic = {'plot_data': {'data': {'x_data': {'values': xdata, 'name': 'x_data', 'unit': 's'},
                              'y_data': {'values': ydata, 'name': 'y_data', 'unit': 'A'}},
                     'meta': {'timestamp_last_sample': 123,
                              'location': 'Deutschland, Oberkochen',
                              'machine': 'some machine',
                              'worker': 'Max Mustermann'},
                     'plot': {'raw': {'figure': [{'subplot': [{'plots': [['x_data', 'y_data']]}]}]}}}}

savemat('data.mat', dic)
