from dataclasses import dataclass, asdict
import numpy as np


@dataclass
class Data:
    values: np.ndarray
    name: str
    unit: str


# create numpy arrays
a = np.arange(15)
b = np.empty((1, 15))
c = np.linspace(0, np.pi * 3, 15)

# create Data objects
t_incremental = Data(a, 'time', 's')
raw_x1 = Data(b, 'current in AD counts', 'A')
raw_x2 = Data(c, 'angle in radiant', 'rad')

print(t_incremental.name, t_incremental.unit)
print(raw_x1.name, raw_x1.unit)
print(raw_x2.name, raw_x2.unit)

# convert to dict
t_incremental_dict = asdict(t_incremental)
raw_x1_dict = asdict(raw_x1)
raw_x2_dict = asdict(raw_x2)

print(t_incremental_dict)
print(raw_x1_dict)
print(raw_x2_dict)

# convert dict back to Data object
t_incremental = Data(**t_incremental_dict)
raw_x1 = Data(**raw_x1_dict)
raw_x2 = Data(**raw_x2_dict)

print(t_incremental)
print(raw_x1)
print(raw_x2)
