import numpy as np
from scipy.io import savemat

t_incremental = np.linspace(0.1, 20.1, 200)

raw_x1 = np.tan(t_incremental) * ((np.random.rand(1, len(t_incremental)) + 0.5) * 0.5)
raw_x2 = np.sqrt(t_incremental) * ((np.random.rand(1, len(t_incremental)) + 0.5) * 0.5)
raw_x3 = np.log(t_incremental) * ((np.random.rand(1, len(t_incremental)) + 0.5) * 0.5)

d1 = {'trace': {'data': {'raw_force': {'values': raw_x1, 'name': 'Force', 'unit': 'N'},
                         'raw_current': {'values': raw_x2, 'name': 'Current', 'unit': 'A'},
                         'raw_voltage': {'values': raw_x3, 'name': 'Voltage', 'unit': 'V'},
                         't_incremental': {'values': t_incremental, 'name': 'Time in s', 'unit': 's'}},
                'meta': {'timestamp_last_sample': 123456.789,
                         'location': 'Deutschland, Oberkochen',
                         'machine': 'bla',
                         'worker': 'Max Mustermann'},
                'plot': {'raw': {'fig1': {'title': 'Title of fig1'},
                                 'fig2': {}},
                         'frequency': {
                                 'fig1': {},
                                 'fig2': {}}}}}

d2 = {'trace': {'data': {'raw_force': {'values': raw_x1, 'name': 'Force', 'unit': 'N'},
                         'current': {'values': raw_x2, 'name': 'Current', 'unit': 'A'},
                         'raw_voltage': {'values': raw_x3, 'name': 'Voltage', 'unit': 'V'},
                         't_incremental': {'values': t_incremental, 'name': 'Time in s', 'unit': 's'},
                         'static': False},
                'meta': {'timestamp_last_sample': 123456.789,
                         'location': 'Deutschland, Oberkochen',
                         'machine': 'bla',
                         'worker': 'Max Mustermann',
                         'static': True},
                'plot': {'raw': [{'title': 'Title of fig1'}, {}],
                         'frequency': [{}, {}],
                         'static': False},
                'static': True}}

savemat('data.mat', d2)
