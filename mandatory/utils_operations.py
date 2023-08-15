import random
from utils_colors import Colors
from class_matrix import Matrix
from class_vector import Vector
from utils_constants import MIN_COORD, MAX_COORD

def reshape(x):
    if isinstance(x, Vector):
        return Matrix(x.coordinates)
    elif isinstance(x, Matrix):
        v = []
        for c in x.columns:
            v.extend(c)
        return Vector(*v)

def matrix_from_shape(rows, cols, fill_with=None):
    if fill_with:
        params = [[fill_with for _ in range(cols)] for _ in range(rows)]
    else:
        params = [[float(random.randrange(MIN_COORD, MAX_COORD)) for _ in range(cols)] for _ in range(rows)]
    return Matrix(*params)

def vector_from_size(size, fill_with=None):
    if fill_with:
        params = [fill_with for _ in range(size)]
    else:
        params = [float(random.randrange(MIN_COORD, MAX_COORD)) for _ in range(size)]
    return Vector(*params)

def linear_combination(vectors, coefs):
    dim = vectors[0].size()
    res_coords = [0] * dim
    for v, coef in zip(vectors, coefs):
        for i in range(dim):
            res_coords[i] += v.coordinates[i] * coef
    return Vector(*res_coords)

def lerp(x, y, t):
    return x * (1 - t) + (y * t)
