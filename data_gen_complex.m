phi = 12 * pi * [0 : 999] / 1000;
mu = 100;
sigma = 15;

time = [0 : 999] / 1000;
raw_force = tan(time);
current = sqrt(time);
raw_voltage = log(time);
x_hist = mu + sigma * randn(100)

plot_data.data.raw_force.values = raw_force;
plot_data.data.raw_force.name = 'Raw Force';
plot_data.data.raw_force.unit = 'N';

plot_data.data.current.values = current;
plot_data.data.current.name = 'Current';
plot_data.data.current.unit = 'A';

plot_data.data.raw_voltage.values = raw_voltage;
plot_data.data.raw_voltage.name = 'Raw Voltage';
plot_data.data.raw_voltage.unit = 'V';

plot_data.data.phi.values = phi;
plot_data.data.phi.name = 'phi';
plot_data.data.phi.unit = 'rad';

plot_data.data.time.values = time;
plot_data.data.time.name = 'time';
plot_data.data.time.unit = 's';

plot_data.data.hist.values = x_hist;
plot_data.data.hist.name = 'hist';
plot_data.data.hist.unit = 'IQ';

plot_data.meta.timestamp_last_sample = 123;
plot_data.meta.location = 'Deutschland, Oberkochen';
plot_data.meta.machine = 'some machine';
plot_data.meta.worker = 'Max Mustermann';

plot_data.plot.raw.figure{1}.subplot_cols = 2;
plot_data.plot.raw.figure{1}.subplot_rows = 2;
plot_data.plot.raw.figure{1}.subplot{1}.plots = {{'time', 'raw_force'}, {'time', 'current'}};
plot_data.plot.raw.figure{1}.subplot{1}.x_label = 'X-Axis of plot 1';
plot_data.plot.raw.figure{1}.subplot{1}.plot_type = 'LinLin';
plot_data.plot.raw.figure{1}.subplot{1}.title = 'subplot 1';
plot_data.plot.raw.figure{1}.subplot{1}.legend = 'lower left';

plot_data.plot.raw.figure{1}.subplot{2}.plots = {'time', 'raw_voltage'};

plot_data.plot.raw.figure{1}.subplot{3}.plots = {'time', 'raw_force'};
plot_data.plot.raw.figure{1}.subplot{3}.grid = false;

plot_data.plot.raw.figure{1}.subplot{4}.plots = {'time', 'current'};
plot_data.plot.raw.figure{1}.subplot{4}.plot_type = 'LinLog';

plot_data.plot.raw.figure{2}.subplot_rows = 2;
plot_data.plot.raw.figure{2}.subplot{1}.plots = {'time', 'raw_voltage'};
plot_data.plot.raw.figure{2}.subplot{2}.plots = {'time', 'current'};
plot_data.plot.raw.figure{2}.subplot{2}.regression = 'Root';

plot_data.plot.raw.figure{3}.subplot{1}.plots = {'phi', 'time'};
plot_data.plot.raw.figure{3}.subplot{1}.plot_type = 'Polar';
plot_data.plot.raw.figure{3}.subplot{1}.title = 'example of polar plot';

plot_data.plot.raw.figure{4}.subplot_cols = 2;
plot_data.plot.raw.figure{4}.subplot{1}.plots = {'hist'};
plot_data.plot.raw.figure{4}.subplot{1}.x_label = 'IQ';
plot_data.plot.raw.figure{4}.subplot{1}.plot_type = 'Hist';
plot_data.plot.raw.figure{4}.subplot{1}.title = 'example of histogram';
plot_data.plot.raw.figure{4}.subplot{1}.bins = 20;
plot_data.plot.raw.figure{4}.subplot{2}.plots = {'hist'};
plot_data.plot.raw.figure{4}.subplot{2}.plot_type = 'Hist';
plot_data.plot.raw.figure{4}.subplot{2}.title = 'second histogram';
plot_data.plot.raw.figure{4}.subplot{2}.bins = 50;
plot_data.plot.raw.figure{4}.subplot{2}.x_label = 'IQ';

plot_data.plot.raw.linkaxes = {{0, 0}, {0, 2}, {1, 0}};

save('-v6', 'data.mat', 'plot_data');