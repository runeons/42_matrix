import math
from utils_colors import Colors
from class_matrix import Matrix

def projection(fov, ratio, near, far):
    if (far <= near):
        raise ValueError(f"{Colors.ERROR}Error: {Colors.RES} far must be behind near.")
    fov = fov * 3.141592653589793 / 180 # to radians
    x = ratio * (1 / math.tan(fov / 2))
    y = 1 / math.tan(fov / 2)
    z = -(far + near) / (far - near)
    w = -(2 * far * near) / (far - near)
    P = Matrix([
        [x, 0., 0., 0.],
        [0., y, 0., 0.],
        [0., 0., z, w],
        [0., 0., 1., 0.],
    ])
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
    f = open("matrix_display/proj", "w+")
    f.write(s)
    f.close()
