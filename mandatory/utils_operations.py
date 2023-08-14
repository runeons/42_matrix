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
