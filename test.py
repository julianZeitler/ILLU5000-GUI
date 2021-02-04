from scipy.io import loadmat, savemat
import numpy as np
from dataclasses import dataclass, asdict

@dataclass
class myClass:
    one: str
    two: int
    three: float

a = myClass('a', 1, 1.5)
print(a)
b = asdict(a)
print(b)

@dataclass
class readClass:
    one: str
    two: int
    three: float

d = readClass(**b)

print(d)

'''
@dataclass
class Wrapped:
    __annotations__ = {k: type(v) for k, v in b.items()}


c = Wrapped()

print(c)
'''
