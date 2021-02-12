import numpy as np
from scipy.io import savemat

t_incremental = np.linspace(0.1, 20.1, 200)

raw_x1 = np.tan(t_incremental) * ((np.random.rand(1, len(t_incremental)) + 0.5) * 0.5)
raw_x2 = np.sqrt(t_incremental) * ((np.random.rand(1, len(t_incremental)) + 0.5) * 0.5)
raw_x3 = np.log(t_incremental) * ((np.random.rand(1, len(t_incremental)) + 0.5) * 0.5)


d2 = {'plot_data': {'data': {'raw_force': {'values': raw_x1, 'name': 'Force', 'unit': 'N'},
                             'current': {'values': raw_x2, 'name': 'Current', 'unit': 'A'},
                             'raw_voltage': {'values': raw_x3, 'name': 'Voltage', 'unit': 'V'},
                             't_incremental': {'values': t_incremental, 'name': 'Time in s', 'unit': 's'},
                             'dyn': True},
                    'meta': {'timestamp_last_sample': 123456.789,
                             'location': 'Deutschland, Oberkochen',
                             'machine': 'bla',
                             'worker': 'Max Mustermann'},
                    'plot': {'raw': [{'title': 'Title of fig1',
                                      'subplot': [{'plots': [['t_incremental', 'raw_force'],
                                                             ['t_incremental', 'current']],
                                                   'x_label': 'X-Axis of plot 1'},

                                                  {'plots': [['t_incremental', 'raw_voltage']]}]},

                                     {'title': 'Title of fig2',
                                      'subplot': [{'plots': []},
                                                  {'plots': []}]}],

                             'frequency': [{'subplot': [{'plots': [], 'x_label': 'test label'}]},
                                           {'subplot': [{'plots': []}, {'plots': []}]}],
                             'dyn': True}}}

savemat('data.mat', d2)
