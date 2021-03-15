
phi = 12 * pi * [0 : 999] / 1000;
mu = 100;
sigma = 15;

raw_force = tan(time);
current = sqrt(time);
raw_voltage = log(time);
x_hist = mu + sigma * randi(10000);

plot_data.data = struct('raw_force', struct('values', raw_force, 'name', 'Raw Force', 'unit', 'N'),
                        'current', struct('values', current, 'name', 'Current', 'unit', 'A'),
                        'raw_voltage', struct('values', raw_voltage, 'name', 'Raw Voltage', 'unit', 'V'),
                        'phi', struct('values', phi, 'name', 'Phi', 'unit', 'rad'),
                        'time', struct('values', time, 'name', 'time', 'unit', 's'),
                        'hist', struct('values', x_hist, 'name', 'hist', 'unit', 'IQ'))

plot_data.meta = struct('timestamp_last_sample', 123,
                        'location', 'Deutschland, Oberkochen',
                        'machine', 'some machine',
                        'worker', 'Max Mustermann')

plot_data.plot.raw.figure{1} = struct('subplot_cols', 2,
                                      'subplot_rows', 2,
                                      'subplot', {struct('plots', {{'time', 'raw_force'},
                                                                   {'time', 'current'}},
                                                         'x_label', 'X-Axis of plot 1',
                                                         'plot_type', 'LinLin',
                                                         'title', 'subplot 1',
                                                         'legend', 'lower left'),
                                                  struct('plots', {'time', 'raw_voltage'},
                                                         'plot_type', 'LinLog'),
                                                  struct('plots', {'time', 'raw_force'},
                                                         'grid', false),
                                                  struct('plots', {'time', 'raw_voltage'})})

plot_data.plot.raw.figure{2} = struct('subplot_rows', 2,
                                       'subplot', {struct('plots', {'time', 'raw_voltage'}),
                                                   struct('plots', {'time', 'current'},
                                                          'regression', 'Root')})

plot_data.plot.raw.figure{3} = struct('subplot', {struct('plots', {'phi', 'time'},
                                                          'plot_type', 'Polar',
                                                          'title', 'example of polar plot')})
plot_data.plot.raw.figure{4} = struct('subplot_cols', 2,
                                       'subplot', {struct('plots', {'hist'},
                                                          'x_label', 'IQ',
                                                          'plot_type', 'Hist',
                                                          'title', 'example for histogram',
                                                          'bins', 20,
                                                          'x_label', 'IQ'),

                                                   struct('plots', {'hist'},
                                                          'plot_type', 'Hist',
                                                          'title', 'second histogram',
                                                          'bins', 50,
                                                          'x_label', 'IQ')})
plot_data.plot.raw.linkaxes = {{0, 0}, {0, 2}, {1, 0}}

save('-v6', 'data.mat', 'plot_data');