import random
from utils_colors import Colors
from class_matrix import Matrix
from class_vector import Vector

def reshape(x):
    if isinstance(x, Vector):
        return Matrix(x.coordinates)
    elif isinstance(x, Matrix):
        v = []
        for c in x.columns:
            v.extend(c)
        return Vector(*v)

def matrix_from_shape(rows, cols):
    params = [[float(random.randrange(0, 10)) for _ in range(cols)] for _ in range(rows)]
    return Matrix(*params)