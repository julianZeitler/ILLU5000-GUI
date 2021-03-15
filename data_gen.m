phi = 12 * pi * [0 : 999] / 1000;
sinus = sin(phi);

plot_data.data.phi.values = phi;
plot_data.data.phi.name = 'phi';
plot_data.data.phi.unit = 'rad';

plot_data.data.sinus.values = sinus;
plot_data.data.sinus.name = 'sinus';
plot_data.data.sinus.unit = 'm';

plot_data.meta.timestamp_last_sample = 123;
plot_data.meta.location = 'Deutschland, Oberkochen';
plot_data.meta.machine = 'some machine';
plot_data.meta.worker = 'Max Mustermann';

plot_data.plot.trig.figure{1}.subplot{1}.plots = {{'phi', 'sinus'}};

save('-v6', 'data.mat', 'plot_data');
