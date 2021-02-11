# Overview:

The ILLU GUI is the user interface for the Illuminator 5000. It is written in Python, but the data is read in from \*.mat files.

# Usage:

## execute the program:

```python3 main.py```


## Data format:

The plot data is stored inside a dataclass, which also contains meta information
the dataclass looks like this:

```python
@dataclass
class Data:
    values: np.ndarray
    name: str
    unit: str
```

`Data` can later be tailored to the specific needs.
`values` contains the sensor data and is of type numpy array

When read from the matlab file, the data is in form of a nested dictionary. Each plot is represented by a `key:value` pair. `key` is the name of the plot, `value` is another dictionary, which contains the information, that is later used to instanciate a Data object. The dictionary gets unpacked by the `LoadMat` class in `cl_load.py`.
