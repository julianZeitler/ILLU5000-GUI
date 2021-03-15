time = [0 : 999] / 1000;
phi = 12 * pi * [0 : 999] / 1000;
mu = 100;
sigma = 15;

raw_force = tan(time);
current = sqrt(time);
raw_voltage = log(time);
x_hist = mu + sigma * randi(10000);

plot_data = struct('data', struct('raw_force', struct('values', raw_force, 'name', 'Raw Force', 'unit', 'N'),
                                  'current', struct('values', current, 'name', 'Current', 'unit', 'A'),
                                  'raw_voltage', struct('values', raw_voltage, 'name', 'Raw Voltage', 'unit', 'V'),
                                  'phi', struct('values', phi, 'name', 'Phi', 'unit', 'rad'),
                                  'time', struct('values', time, 'name', 'time', 'unit', 's'),
                                  'hist', struct('values', x_hist, 'name', 'hist', 'unit', 'IQ')),

                   'meta', struct('timestamp_last_sample', 123,
                                  'location', 'Deutschland, Oberkochen',
                                  'machine', 'some machine',
                                  'worker', 'Max Mustermann'))
save("-v6", "data.mat", "plot_data");
