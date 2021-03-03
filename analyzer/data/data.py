"""This module creates a mat file from the dictionary specified in it."""

import numpy as np
from scipy.io import savemat


def data_mat(name):
    """This function utilizes the `scipy.io.savemat()` method to create mat files"""

    t_incremental = np.linspace(0.1, 20.1, 200)
    rad = np.linspace(0, 2, 200)
    theta = 2 * np.pi * rad
    mu, sigma = 100, 15

    raw_force = np.tan(t_incremental) * ((np.random.rand(1, len(t_incremental)) + 0.5) * 0.5)
    current = np.sqrt(t_incremental) * ((np.random.rand(1, len(t_incremental)) + 0.5) * 0.5)
    raw_voltage = np.log(t_incremental) * ((np.random.rand(1, len(t_incremental)) + 0.5) * 0.5)
    x_hist = mu + sigma * np.random.randn(10000)

    d1 = {'plot_data': {'data': {'raw_force': {'values': raw_force, 'name': 'Raw Force', 'unit': 'N'},
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
                        'plot': {'raw': {'figure': [{'title': 'Title of fig1',
                                                     'subplot_cols': 2,
                                                     'subplot_rows': 2,
                                                     'subplot': [{'plots': [['t_incremental', 'raw_force'],
                                                                            ['t_incremental', 'current']],
                                                                  'x_label': 'X-Axis of plot 1',
                                                                  'plot_type': 'LinLin',
                                                                  'title': 'subplot 1',
                                                                  'legend': 'lower left'},

                                                                 {'plots': [['t_incremental', 'raw_voltage']],
                                                                  'plot_type': 'LinLog'},
                                                                 {'plots': [['t_incremental', 'raw_force']],
                                                                  'grid': False},
                                                                 {'plots': [['t_incremental', 'raw_voltage']]}]},

                                                    {'title': 'Title of fig2',
                                                     'subplot_rows': 2,
                                                     'subplot': [{'plots': [['t_incremental', 'raw_voltage']]},
                                                                 {'plots': [['t_incremental', 'current']],
                                                                  'regression': 'Root'}]},

                                                    {'subplot': [{'plots': [['theta', 'rad']],
                                                                  'plot_type': 'Polar',
                                                                  'title': 'example polar plot'}]},

                                                    {'subplot_cols': 2,
                                                     'subplot': [{'plots': ['hist'],
                                                                  'plot_type': 'Hist',
                                                                  'title': 'example for histogram',
                                                                  'bins': 20,
                                                                  'x_label': 'IQ'},

                                                                 {'plots': ['hist'],
                                                                  'plot_type': 'Hist',
                                                                  'title': 'example for second histogram',
                                                                  'bins': 50,
                                                                  'x_label': 'IQ'}]}],
                                         'linkaxes': [[0, 0], [0, 2], [1, 0]]}}}}
    savemat(name, d1)
