from utils_colors import Colors

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

class Matrix:
    def __init__(self, *rows):
        self.rows = [list(row) for row in rows]

    def __str__(self):
        s = f"{Colors.PINK}MATRIX:{Colors.RES}\n"
        if not len(self.rows):
            s += "[]\n"
            return s
        max_width = max([max(len(str(entry)) for entry in row) for row in self.rows])
        for row in self.rows:
            s += "[ "
            for i, entry in enumerate(row):
                s += f"{entry:<{max_width}}"
                if i != len(row) - 1:
                    s += ", "
            s += " ]\n"
        return s

def main():
    tests_vectors = [
        (0., 1., 2.),
        (2.,),
        (),
        (3.14, 2.71, 1.618),
        (3.14, 2.71, 1.618, 3., 4., 5.),
        ("a", "b", "cde"),
    ]
    tests_matrixes = [
        [[1., 2.], [3., 4.]],
        [[1, 2, 3], [4, 5, 6]],
        [[7, 8], [9, 10], [11, 12]],
    ]
    for t in tests_vectors:
        v = Vector(*t)
        print(v)
    for t in tests_matrixes:
        v = Matrix(*t)
        print(v)

if (__name__ == "__main__"):
    main()