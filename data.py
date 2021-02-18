import numpy as np
from scipy.io import savemat

t_incremental = np.linspace(0.1, 20.1, 200)

raw_force = np.tan(t_incremental) * ((np.random.rand(1, len(t_incremental)) + 0.5) * 0.5)
current = np.sqrt(t_incremental) * ((np.random.rand(1, len(t_incremental)) + 0.5) * 0.5)
raw_voltage = np.log(t_incremental) * ((np.random.rand(1, len(t_incremental)) + 0.5) * 0.5)

d1 = {'plot_data': {'data': {'raw_force': {'values': raw_force, 'name': 'Raw Force', 'unit': 'N'},
                             'current': {'values': current, 'name': 'Current', 'unit': 'A'},
                             'raw_voltage': {'values': raw_voltage, 'name': 'Raw Voltage', 'unit': 'V'},
                             't_incremental': {'values': t_incremental, 'name': 'Time incremental', 'unit': 's'}},

                    'meta': {'timestamp_last_sample': 12345.6789,
                             'location': 'Deutschland, Oberkochen',
                             'machine': 'bla',
                             'worker': 'Max Mustermann'},
                    'plot': {'raw': {'figure': [{'title': 'Title of fig1',
                                                 'subplot_cols': 2,
                                                 'subplot_rows': 2,
                                                 'subplot': [{'plots': [['t_incremental', 'raw_force'],
                                                                        ['t_incremental', 'current']],
                                                              'x_label': 'X-Axis of plot 1',
                                                              'plot_type': 'LinLog',
                                                              'title': 'subplot 1',
                                                              'legend': 'lower left'},

                                                             {'plots': [['t_incremental', 'raw_voltage']]},
                                                             {'plots': [['t_incremental', 'raw_force']]},
                                                             {'plots': [['t_incremental', 'raw_voltage']]}]},

                                                {'title': 'Title of fig2',
                                                 'subplot_rows': 2,
                                                 'subplot': [{'plots': [['t_incremental', 'raw_voltage']]},
                                                             {'plots': [['t_incremental', 'current']]}]}]},

                             'frequency': {'figure': [{'subplot': [{'plots': [], 'x_label': 'test label'}]},
                                                      {'subplot': [{'plots': []}, {'plots': []}]}]}}}}


def data_mat():
    savemat('data.mat', d1)
