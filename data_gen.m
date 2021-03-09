xdata = 12 * pi * [0 : 999] / 1000;
ydata = sin(xdata);

x_data.values = xdata;
x_data.name = 'x_data';
x_data.unit = 's';

y_data.values = ydata;
y_data.name = 'y_data';
y_data.unit = 'A';

data.x_data = x_data;
data.y_data = y_data;

meta.timestamp_last_sample = 123;
meta.location = 'Deutschland, Oberkochen';
meta.machine = 'some machine';
meta.worker = 'Max Mustermann';

subplot1.plots = [['x_data', 'y_data']];
fig1.subplot = [subplot1];
figure = [fig1];

raw.figure = figure;
raw.linkaxes = [[0, 0]];
plot.raw = raw;


plot_data.data = data;
plot_data.meta = meta;
plot_data.plot = plot;

save("-v6", "data.mat", "plot_data");
