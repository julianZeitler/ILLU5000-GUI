# Overview:

The ILLU GUI is the user interface for the Illuminator 5000. It is written in Python, but the data is read in from \*.mat files.

# Usage:

## execute the program:

[...]


## Data format:

the data is read from a matlab file and is then written into nested classes. The Syntax for accessing each item looks like this:


```python
top.plot_data.data['raw_force'].values
top.plot_data.data['raw_force'].name
top.plot_data.data['raw_force'].unit

top.plot_data.meta.timestamp_last_sample
top.plot_data.meta.location
top.plot_data.meta.machine
top.plot_data.meta.worker

top.plot_data.plot['raw'].figure[0].title
top.plot_data.plot['raw'].figure[0].subplot[0].x_label
top.plot_data.plot['raw'].figure[0].subplot[0].plot_type
```

