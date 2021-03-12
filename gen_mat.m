time = [0 : 999] / 1000;
phi = 12 * pi * [0 : 999] / 1000;
mu = 100;
sigma = 15;

raw_force = tan(time);
current = sqrt(time);
raw_voltage = log(time);
x_hist = mu + sigma * randi(10000);

file_data = struct('plot_data', struct('data', struct('raw_force', struct('values', raw_force, 'name', 'Raw Force', 'unit', 'N'),
                                                      'current', struct('values', current, 'name', 'Current', 'unit', 'A'),
                                                      'raw_voltage', struct('values', raw_voltage, 'name', 'Raw Voltage', 'unit', 'V'),
                                                      'phi', struct('values', phi, 'name', 'Phi', 'unit', 'rad'),
                                                      'time', struct('values', time, 'name', 'time', 'unit', 's'),
                                                      'hist', struct('values', x_hist, 'name', 'hist', 'unit', 'IQ')),

                                       'meta', struct('timestamp_last_sample', 123,
                                                      'location', 'Deutschland, Oberkochen',
                                                      'machine', 'some machine',
                                                      'worker', 'Max Mustermann'),

                                       'plot', struct('raw', struct('figure', [struct('subplot_cols', 2,
                                                                                      'subplot_rows', 2,
                                                                                      'subplot', [struct('plots', [['time', 'raw_force'],
                                                                                                                   ['time', 'current']],
                                                                                                         'x_label', 'X-Axis of plot 1',
                                                                                                         'plot_type', 'LinLin',
                                                                                                         'title', 'subplot 1',
                                                                                                         'legend', 'lower left'),
                                                                                                  struct('plots', ['time', 'raw_voltage'],
                                                                                                         'plot_type', 'LinLog'),
                                                                                                  struct('plots', ['time', 'raw_force'],
                                                                                                         'grid', false),
                                                                                                  struct('plots', ['time', 'raw_voltage'])]),

                                                                               struct('subplot_rows', 2,
                                                                                      'subplot', [struct('plots', ['time', 'raw_voltage']),
                                                                                                  struct('plots', ['time', 'current'],
                                                                                                         'regression', 'Root')]),

                                                                               struct('subplot', [struct('plots', ['phi', 'time'],
                                                                                                         'plot_type', 'Polar',
                                                                                                         'title', 'example of polar plot')]),
                                                                               struct('subplot_cols', 2,
                                                                                      'subplot', [struct('plots', hist,
                                                                                                         'x_label', 'IQ')])]))))
                                                                                                         'x_label', 'IQ')])]))))
                                                                                                         'plot_type', 'Hist',
                                                                                                         'title', 'example for histogram',
                                                                                                         'bins', 20,
                                                                                                         'x_label', 'IQ'),

                                                                                                  struct('plots', hist,
                                                                                                         'plot_type', 'Hist',
                                                                                                         'title', 'second histogram',
                                                                                                         'bins', 50,
                                                                                                         'x_label', 'IQ')])]))))
