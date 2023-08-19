import random
from utils_colors import Colors
from class_matrix import Matrix
from class_vector import Vector
from utils_constants import MIN_COORD, MAX_COORD
from utils_display import space_complexity

def reshape(x):
    if isinstance(x, Vector):
        return Matrix(x.coordinates)
    elif isinstance(x, Matrix):
        v = []
        for j in range(x.shape()[1]):
            for i in range(x.shape()[0]):
                v.append(x.rows[i][j])
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

@space_complexity
def linear_combination(vectors, coefs):
    dim = vectors[0].size()
    res_coords = [0] * dim
    for v, coef in zip(vectors, coefs):
        for i in range(dim):
            res_coords[i] += v.coordinates[i] * coef
    return Vector(*res_coords)

@space_complexity
def lerp(x, y, t):
    return x * (1 - t) + (y * t)

@space_complexity
def angle_cos(u, v):
    return u.dot(v) / (u.norm() * v.norm())

def cross_product(u, v):
    res_coords = [0, 0, 0]
    gamma = [(1, 2), (0, 2), (0, 1)]
    for i in range(3):
        res_coords[i] = (u.coordinates[gamma[i][0]] * v.coordinates[gamma[i][1]] - u.coordinates[gamma[i][1]] * v.coordinates[gamma[i][0]]) * (-1) ** i
    return Vector(*res_coords)
