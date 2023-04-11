# mylib.py

import ctypes

# Load the shared library
mylib = ctypes.cdll.LoadLibrary('./lib/mylib.so')

# Define the argument and return types for the `myadd` function
mylib.myadd.argtypes = [ctypes.c_int, ctypes.c_int]
mylib.myadd.restype = ctypes.c_int

# Define the `Point` class in Python
class Point:
    def __init__(self, x, y):
        self.obj = mylib.Point(x, y)

    def print(self):
        mylib.Point_print(self.obj)

# Test the module
print(mylib.myadd(1, 2))  # Output: 3

p = Point(3, 4)
p.print()  # Output: (3, 4)
