import math
from utils_colors import Colors
from class_matrix import Matrix

def projection(fov, ratio, near, far):
    if (far - near == 0):
        raise ValueError(f"{Colors.ERROR}Error: {Colors.RES} far and near planes can't be equal.")
    x = ratio * (1 / math.tan(fov / 2))
    y = 1 / math.tan(fov / 2)
    z = far / (far - near)
    w = -near * (far / (far  - near))

    P = Matrix(
        [x, 0., 0., 0.],
        [0., y, 0., 0.],
        [0., 0., z / w, -1.],
        [0., 0., 1., 0.],
    )
    return P

def to_string(m: Matrix):
    s = ""
    for i, row in enumerate(m.rows):
        for j, coord in enumerate(row):
            s += f"{coord}"
            if j != len(row) - 1:
                s += ", "
        s += "\n"
    return s
    
def to_file(m: Matrix):
    s = to_string(m)
    f = open("display_macos/proj", "w+")
    f.write(s)
    f.close()
