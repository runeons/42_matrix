from utils_colors import Colors
from utils_display import space_complexity
import numpy as np

class Vector:
    def __init__ (self, *coordinates):
        self.coordinates = list(*coordinates)
        self.check_validity()
    
    def check_validity(self):
        if not len(self.coordinates):
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}{self.coordinates} is not a valid vector.")

    def __str__(self):
        return(str(self.coordinates))
    
    def summary(self):
        s = f"{Colors.VECTOR}VECTOR:{Colors.RES}\n"
        if not len(self.coordinates):
            s += "[]\n"
            return s
        max_width = max(len(str(coord)) for coord in self.coordinates)
        for i, coord in enumerate(self.coordinates):
            s += f"[ {str(coord):<{max_width}} ]"
            if i != len(self.coordinates) - 1:
                s += "\n"
        print(s)
        print(f"{Colors.VECTOR}size: {Colors.RES}{self.size()}")
        print()

    def __eq__(self, v):
        if isinstance(v, Vector):
            if (self.coordinates == v.coordinates):
                return True
            else:
                return False
        elif isinstance(v, np.ndarray):
            if (np.array_equal(self.coordinates, v)):
                return True
            else:
                return False            
        else:
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}cannot compare Vector with non-Vector.")
        
    def __add__(self, v):
        if isinstance(v, Vector) and self.size() == v.size():
            # res = [(i[0] + j[0], i[1] + j[1]) for i, j in zip(self.coordinates, v.coordinates)]
            res = [ i + j for i, j in zip(self.coordinates, v.coordinates) ]
            return Vector(res)
        else:
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Vectors should have the same dimension to use operator +.")

    def __sub__(self, v):
        if isinstance(v, Vector) and self.size() == v.size():
            res = [x1 - x2 for x1, x2 in zip(self.coordinates, v.coordinates)]
            return Vector([*res])
        else:
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Vectors should have the same dimension to use operator -.")

    def __mul__(self, scalar):
        if (isinstance(scalar, int) or isinstance(scalar, float)):
            return self.scl(scalar)
        else:
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Vector multiplication not implemented.")

    def __div__(self, scalar):
        if (isinstance(scalar, int) or isinstance(scalar, float)):
            return self.scl(1 / scalar)
        else:
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Vector multiplication not implemented.")

    def size(self):
        return len(self.coordinates)

    # [(5, 3)], [(4, 2)]), [(9, 5)]
    @space_complexity
    def add(self, v: 'Vector'):
        if self.size() != v.size():
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Cannot add two vectors of different sizes.")
        res = [ i + j for i, j in zip(self.coordinates, v.coordinates) ]
        # res = [(i[0] + j[0], i[1] + j[1]) for i, j in zip(self.coordinates, v.coordinates)]
        return Vector(res)

    @space_complexity
    def sub(self, v: 'Vector'):
        if self.size() != v.size():
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Cannot add two vectors of different sizes.")
        res = [ i - j for i, j in zip(self.coordinates, v.coordinates) ]
        # return Vector([*res])
        # res = [(i[0] + j[0], i[1] + j[1]) for i, j in zip(self.coordinates, v.coordinates)]
        return Vector(res)

    @space_complexity
    def scl(self, scalar):
        res = [i * scalar for i in self.coordinates]
        return Vector([*res])

    @space_complexity
    def dot(self, v):
        if self.size() != v.size():
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Cannot dot two vectors of different sizes.")
        dot = 0.
        for i, j in zip(self.coordinates, v.coordinates):
            dot += i * j
        return dot

    def _abs(self, x):
        if x < 0:
            return -x
        return x

    @space_complexity
    def norm_1(self):
        norm = 0.
        for i in self.coordinates:
            norm += self._abs(i)
        return norm

    @space_complexity
    def norm(self):
        norm = 0.
        for c in self.coordinates:
            r2 = c.real * c.real
            i2 = c.imag * c.imag
            norm += r2 + i2
        return norm ** 0.5

    @space_complexity
    def norm_inf(self):
        norm = max([self._abs(i) for i in self.coordinates])
        return norm
