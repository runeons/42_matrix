from utils_colors import Colors
from class_matrix import Matrix

class Vector:
    def __init__ (self, *coordinates):
        self.coordinates = list(coordinates)
    
    def __str__(self):
        s = f"{Colors.BLUE}VECTOR:{Colors.RES}\n"
        if not len(self.coordinates):
            s += "[]\n"
            return s
        max_width = max(len(str(coord)) for coord in self.coordinates)
        for coord in self.coordinates:
            s += f"[ {coord:<{max_width}} ]\n"
        return s
    
    def size(self):
        return len(self.coordinates)

    def to_matrix(self):
        return Matrix(self.coordinates)

    def add(self, v: 'Vector'):
        if len(self.coordinates) != len(v.coordinates):
            raise ValueError("Vector addition can only be operated on vectors with the same dimension.")
        print(v)

