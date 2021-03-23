from DataAnalyzer.Data.cl_data import FileData
from DataAnalyzer.Functions.func_mat import save
from DataAnalyzer.Plot.cl_plot import Plot

import numpy as np
from matplotlib.pyplot import show

t_incremental = np.linspace(0.1, 20.1, 200)
rad = np.linspace(0, 2, 200)
theta = 2 * np.pi * rad
mu, sigma = 100, 15

raw_current = np.tan(t_incremental) * ((np.random.rand(1, len(t_incremental)) + 0.5) * 0.5)
current = np.sqrt(t_incremental) * ((np.random.rand(1, len(t_incremental)) + 0.5) * 0.5)
raw_voltage = np.log(t_incremental) * ((np.random.rand(1, len(t_incremental)) + 0.5) * 0.5)
x_hist = mu + sigma * np.random.randn(10000)

d1 = {'plot_data': {'data': {'raw_current': {'values': raw_current, 'name': 'Raw Current', 'unit': 'A'},
                             'current': {'values': current, 'name': 'Current', 'unit': 'A'},
                             'raw_voltage': {'values': raw_voltage, 'name': 'Raw Voltage', 'unit': 'V'},
                             'rad': {'values': rad, 'name': 'rad', 'unit': 'm'},
                             'theta': {'values': theta, 'name': 'theta', 'unit': 'rad'},
                             't_incremental': {'values': t_incremental, 'name': 'Time incremental', 'unit': 's'},
                             'hist': {'values': x_hist, 'name': 'hist', 'unit': 'IQ'}},

                    'meta': {'timestamp_last_sample': 12345.6789,
                             'location': 'Deutschland, Oberkochen',
                             'machine': 'bla',
                             'worker': 'Max Mustermann'},
                    'plot': {'raw': {'figure': [{'subplot_cols': 2,
                                                 'subplot_rows': 2,
                                                 'subplot': [{'plots': np.array([['t_incremental', 'raw_current'],
                                                                                 ['t_incremental', 'current']],
                                                                                dtype=object),
                                                              'x_label': 'X-Axis of Plot 1',
                                                              'plot_type': 'LinLin',
                                                              'title': 'subplot 1',
                                                              'legend': 'lower left'},

                                                             {'plots': np.array([['t_incremental', 'raw_voltage']],
                                                                                dtype=object),
                                                              'plot_type': 'LinLog'},
                                                             {'plots': np.array([['t_incremental', 'raw_current']],
                                                                                dtype=object),
                                                              'grid': False},
                                                             {'plots': np.array([['t_incremental', 'raw_voltage']],
                                                                                dtype=object)}]},

                                                {'subplot_rows': 2,
                                                 'subplot': [{'plots': np.array([['t_incremental', 'raw_voltage']],
                                                                                dtype=object)},
                                                             {'plots': np.array([['t_incremental', 'current']],
                                                                                dtype=object),
                                                              'regression': 'Root'}]},

                                                {'subplot': [{'plots': np.array([['theta', 'rad']],
                                                                                dtype=object),
                                                              'plot_type': 'Polar',
                                                              'title': 'example polar Plot'}]},

                                                {'subplot_cols': 2,
                                                 'subplot': [{'plots': np.array([['hist']], dtype=object),
                                                              'plot_type': 'Hist',
                                                              'title': 'example for histogram',
                                                              'bins': 20,
                                                              'x_label': 'IQ'},

                                                             {'plots': np.array([['hist']], dtype=object),
                                                              'plot_type': 'Hist',
                                                              'title': 'example for second histogram',
                                                              'bins': 50,
                                                              'x_label': 'IQ'}]}],
                                     'linkaxes': [[0, 0], [0, 2], [1, 0]]}}}}

file_data = FileData(**d1)

save(file_data, 'data.mat')

Plot('data.mat', 'raw')
show()
