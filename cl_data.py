from dataclasses import dataclass, asdict
import numpy as np

# Data defines the structure of the data, that will be read in


@dataclass
class Data:
    values: np.ndarray
    name: str
    unit: str

