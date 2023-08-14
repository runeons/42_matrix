from utils_colors import Colors

class Vector:
    def __init__ (self, *coordinates):
        self.coordinates = list(coordinates)
        self.check_validity()
    
    def check_validity(self):
        if not len(self.coordinates):
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}{self.coordinates} is not a valid vector.")

    def __str__(self):
        s = f"{Colors.VECTOR}VECTOR:{Colors.RES}\n"
        if not len(self.coordinates):
            s += "[]\n"
            return s
        max_width = max(len(str(coord)) for coord in self.coordinates)
        for i, coord in enumerate(self.coordinates):
            s += f"[ {str(coord):<{max_width}} ]"
            if i != len(self.coordinates) - 1:
                s += "\n"
        return s
    
    def summary(self):
        print(self)
        print(f"{Colors.VECTOR}size: {Colors.RES}{self.size()}")
        print()

    def size(self):
        return len(self.coordinates)

    def add(self, v: 'Vector'):
        if self.size() != v.size():
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Cannot add two vectors of different sizes.")
        res = [ i + j for i, j in zip(self.coordinates, v.coordinates) ]
        return Vector(*res)

    def sub(self, v: 'Vector'):
        if self.size() != v.size():
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Cannot add two vectors of different sizes.")
        res = [ i - j for i, j in zip(self.coordinates, v.coordinates) ]
        return Vector(*res)

    def scl(self, scalar):
        res = [ i * scalar for i in self.coordinates]
        return Vector(*res)

