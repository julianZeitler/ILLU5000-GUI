import numpy as np
from scipy.io import savemat

t_incremental = np.linspace(0.1, 20.1, 200)

raw_x1 = np.tan(t_incremental) * ((np.random.rand(1, len(t_incremental)) + 0.5) * 0.5)
raw_x2 = np.sqrt(t_incremental) * ((np.random.rand(1, len(t_incremental)) + 0.5) * 0.5)
raw_x3 = np.log(t_incremental) * ((np.random.rand(1, len(t_incremental)) + 0.5) * 0.5)

d1 = {'plot_data': {'data': {'raw_force': {'values': raw_x1, 'name': 'Force', 'unit': 'N'},
                             'current': {'values': raw_x2, 'name': 'Current', 'unit': 'A'},
                             'raw_voltage': {'values': raw_x3, 'name': 'Voltage', 'unit': 'V'},
                             't_incremental': {'values': t_incremental, 'name': 'Time in s', 'unit': 's'}},

                    'meta': {'timestamp_last_sample': 12345.6789,
                             'location': 'Deutschland, Oberkochen',
                             'machine': 'bla',
                             'worker': 'Max Mustermann'},
                    'plot': {'raw': {'figure': [{'title': 'Title of fig1',
                                                 'subplot_cols': 2,
                                                 'subplot': [{'plots': [['t_incremental', 'raw_force'],
                                                                        ['t_incremental', 'current']],
                                                              'x_label': 'X-Axis of plot 1',
                                                              'plot_type': 'LinLog',
                                                              'title': 'subplot 1',
                                                              'share_x': '2'},

                                                             {'plots': [['t_incremental', 'raw_voltage']]}]},

                                                {'title': 'Title of fig2',
                                                 'subplot_rows': 2,
                                                 'subplot': [{'plots': [['t_incremental', 'raw_voltage']]},
                                                             {'plots': [['t_incremental', 'current']]}]}]},

                             'frequency': {'figure': [{'subplot': [{'plots': [], 'x_label': 'test label'}]},
                                                      {'subplot': [{'plots': []}, {'plots': []}]}]}}}}

d2 = {'plot_data': {'data': {'raw_force': {'values': raw_x1, 'name': 'Force', 'unit': 'N'},
                             'current': {'values': raw_x2, 'name': 'Current', 'unit': 'A'},
                             'raw_voltage': {'values': raw_x3, 'name': 'Voltage', 'unit': 'V'},
                             't_incremental': {'values': t_incremental, 'name': 'Time in s', 'unit': 's'}},

                    'meta': {'timestamp_last_sample': 12345.6789,
                             'location': 'Deutschland, Oberkochen',
                             'machine': 'bla',
                             'worker': 'Max Mustermann'},
                    'plot': {'raw': {'figure': [{'title': 'Title of fig1',
                                                 'subplot_rows': 2,
                                                 'subplot': [{'plots': [['t_incremental', 'raw_force'],
                                                                        ['t_incremental', 'current']],
                                                              'x_label': 'X-Axis of plot 1',
                                                              'plot_type': 'LinLog'},

                                                             {'plots': [['t_incremental', 'raw_voltage']]}]},

                                                {'title': 'Title of fig2',
                                                 'subplot_rows': 2,
                                                 'subplot': [{'plots': []},
                                                             {'plots': []}]}]},

                             'frequency': {'figure': [{'subplot': [{'plots': [], 'x_label': 'test label'}]},
                                                      {'subplot': [{'plots': []}, {'plots': []}]}]}}}}

savemat('data.mat', d1)
