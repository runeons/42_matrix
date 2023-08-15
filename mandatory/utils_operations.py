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

def matrix_from_shape(rows, cols, fill_with=None):
    if fill_with:
        params = [[fill_with for _ in range(cols)] for _ in range(rows)]
    else:
        params = [[float(random.randrange(0, 10)) for _ in range(cols)] for _ in range(rows)]
    return Matrix(*params)

def vector_from_size(size, fill_with=None):
    if fill_with:
        params = [fill_with for _ in range(size)]
    else:
        params = [float(random.randrange(0, 10)) for _ in range(size)]
    return Vector(*params)

def linear_combination(vectors, coefs):
    new_vectors = []
    for dim, dim_coef in zip(vectors, coefs):
        new_vectors.append(dim.scl(dim_coef))
    comb = None
    for i, v in enumerate(new_vectors):
        if (i == 0):
            comb = v
        else:
            comb = comb.add(v)
    return comb