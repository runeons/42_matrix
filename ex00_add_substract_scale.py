from matrix import Matrix
from matrix import Vector
from utils_colors import Colors

RED = "\033[31;01m"
GREEN = "\033[32;01m"
YELLOW = "\033[33;01m"
BLUE = "\033[34;01m"
PINK = "\033[35;01m"
CYAN = "\033[36;01m"
WHITE = "\033[39;01m"
RES = "\033[0m"

def print_error(msg ):
    print(RED + "Error:", WHITE, msg, RES)

def print_title(msg):
    padding = "=" * 30
    print(BLUE + padding, msg , padding, RES)

def print_matrix(m, name = "data", color = BLUE, shape=False):
    if (isinstance(m, Matrix) or isinstance(m, Vector)):
        if (shape):
            print(CYAN + "%-15s%s" % ("shape", ":"), m.shape, RES)
        f_data = [[ round(x, 2) for x in elem] for elem in m.data]
        print(color + "%-15s%s" % (name, ":") + RES, f_data)
    else:
        print_error("Cannot print - this is not a valid Matrix/Vector")


print_title("test Matrix constructor")

matrix_params_tests = [
    [["0.0", 1.0], [2.0, 3.0], [4.0, 5.0]],
    (1, -2, 4),
    (1, -2),
    (1, 0),
    (1),
    [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1]],
    [[], [], []],
    [[-1, 1], [1, 1], [1, 1]],
    [[8, 1], [1, 1], [1, 1]],
    [[1], [1], [1]],
    [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
    (3, 2),
]

for p in matrix_params_tests:
    try:
        new_m = Matrix(p)
        print_matrix(new_m, shape=True)
    except ValueError as err:
        print_error(err)


matrix_params = [
    [[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]],
    [[1, 1], [1, 1], [1, 1]],
    [[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]],
    [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
]

matrices = []

print_title("construct matrices")

for p in matrix_params:
    matrices.append(Matrix(p))

for m in matrices:
    print_matrix(m)

print_title("Matrix additions/substractions")
for m1 in matrices:
    for m2 in matrices:
        try:
            print(GREEN + "\nExpected : OK", RES) if (m1.shape == m2.shape) else print(RED + "\nExpected : KO", RES)
            print_matrix(m1, name="m1", color=YELLOW)
            print_matrix(m2, name="m2", color=YELLOW)
            print_matrix(m1 + m2, name="addition")
            print_matrix(m1 - m2, name="substraction")
        except ValueError as err:
            print_error(err)

print_title("Matrix / Scalar division")
m1 = Matrix([[12, 4, 3], [9, 14, 2], [0, -7, 2]])
for n in [(3, 2), 0, -1, 0.2, 2, 2.0, 3, 6, 7]:
    try:
        print(GREEN + "\nExpected : OK", RES) if (type(n) in (int, float) and n != 0) else print(RED + "\nExpected : KO", RES)
        print(YELLOW + "%-15s%s" % ("n", ":"), n, RES)
        print_matrix(m1, name="m1", color=YELLOW)
        print_matrix(m1 / n, name="division")
    except ValueError as err:
        print_error(err)


print_title("Matrix multiplication")
print_title("Matrix multiplication - 3x2 * 2x1")

t1 = Matrix([[1, 3], [4, 0], [2, 1]])
t2 = Matrix([[1], [5]])

print_matrix(t1, name="t1", color=YELLOW)
print_matrix(t2, name="t2", color=YELLOW)
try:
    ret = t1 * t2
    print_matrix(ret, name="multiplication")
    solution = Matrix([[16], [4], [7]])
    print(GREEN + "OK" + RES) if ret.__eq__(solution) else print(RED + "KO" + RES)
except ValueError as err:
    print_error(err)
    
print_title("Matrix multiplication - 2x3 * 3x2")

t1 = Matrix([[1, 3, 2], [4, 0, 1]])
t2 = Matrix([[1, 3], [0, 1], [5, 2]])

print_matrix(t1, name="t1", color=YELLOW)
print_matrix(t2, name="t2", color=YELLOW)
try:
    ret = t1 * t2
    print_matrix(ret, name="multiplication")
    solution = Matrix([[11, 10], [9, 14]])
    print(GREEN + "OK" + RES) if ret.__eq__(solution) else print(RED + "KO" + RES)
except ValueError as err:
    print_error(err)
    
print_title("Matrix multiplication * scalar")

t1 = Matrix([[1, 3, 2], [4, 0, 1]])
for n in (-1, 0, 4):
    try:
        print_matrix(t1, name="t1", color=YELLOW)
        print(YELLOW + "%-15s%s" % ("n", ":"), RES, n)
        ret = t1 * n
        print_matrix(ret, name="multiplication")
        print(BLUE + "---" + RES)
    except ValueError as err:
        print_error(err)

print_title("Matrix multiplication - 3x2 * 2x4")

t1 = Matrix([[1, 2], [3, 4], [5, 6]])
t2 = Matrix([[2, 3, 4, 5], [3, 4, 5, 6]])

print_matrix(t1, name="t1", color=YELLOW)
print_matrix(t2, name="t2", color=YELLOW)
try:
    ret = t1 * t2
    print_matrix(ret, name="multiplication")
    solution = Matrix([[8, 11, 14, 17], [18, 25, 32, 39], [28, 39, 50, 61]])
    print(GREEN + "OK" + RES) if ret.__eq__(solution) else print(RED + "KO" + RES)
except ValueError as err:
    print_error(err)

    
print_title("Matrix transposition")

t1 = Matrix([[1, 2, 0], [3, 5, 9]])

print_matrix(t1, name="t1", color=YELLOW)
try:
    ret = t1.T()
    print_matrix(ret, name="transposition")
    solution = Matrix([[1, 3], [2, 5], [0, 9]])
    print(GREEN + "OK" + RES) if isinstance(ret, Matrix) else print(RED + "KO" + RES)
    print(GREEN + "OK" + RES) if ret.__eq__(solution) else print(RED + "KO" + RES)
except ValueError as err:
    print_error(err)




print_title("test Vector constructor")

vector_params_tests = [
    [[1, "a", 1]],
    [[1, 1, 1], [1, 1, 1]],
    (3, 2),
    (1, 1, 1),
    (0, 1),
    (3, 1),
    (1, 8),
    [[1], [1], [1]],
    [[1, 1, 1]],
]

for p in vector_params_tests:
    try:
        new_v = Vector(p)
        print_matrix(new_v, shape=True)
    except ValueError as err:
        print_error(err)


print_title("Vector multiplication")
print_title("Matrix/Vector multiplication - 3x2 * 2x1")

t1 = Matrix([[1, 3], [4, 0], [2, 1]])
v1 = Vector([[1], [5]])

print_matrix(t1, name="t1", color=YELLOW)
print_matrix(v1, name="v1", color=YELLOW)
try:
    ret = t1 * v1
    print_matrix(ret, name="multiplication")
    solution = Vector([[16], [4], [7]])
    print(GREEN + "OK" + RES) if isinstance(ret, Vector) else print(RED + "KO" + RES)
    print(GREEN + "OK" + RES) if ret.__eq__(solution) else print(RED + "KO" + RES)
except ValueError as err:
    print_error(err)

print_title("Vector multiplication - 3x1 * 1x4")

v1 = Vector([[1], [4], [2]])
v2 = Vector([[1, 5, 1, 5]])

print_matrix(v1, name="v1", color=YELLOW)
print_matrix(v2, name="v2", color=YELLOW)
try:
    ret = v1 * v2
    print_matrix(ret, name="multiplication")
    solution = Matrix([[1, 5, 1, 5], [4, 20, 4, 20], [2, 10, 2, 10]])
    print(GREEN + "OK" + RES) if isinstance(ret, Matrix) else print(RED + "KO" + RES)
    print(GREEN + "OK" + RES) if ret.__eq__(solution) else print(RED + "KO" + RES)
except ValueError as err:
    print_error(err)
    
print_title("Vector addition - 3x1 + 3x1")

v1 = Vector([[1], [4], [2]])
v2 = Vector([[1], [4], [2]])

print_matrix(v1, name="v1", color=YELLOW)
print_matrix(v2, name="v2", color=YELLOW)
try:
    ret = v1 + v2
    print_matrix(ret, name="addition")
    solution = Vector([[2], [8], [4]])
    print(GREEN + "OK" + RES) if isinstance(ret, Vector) else print(RED + "KO" + RES)
    print(GREEN + "OK" + RES) if ret.__eq__(solution) else print(RED + "KO" + RES)
except ValueError as err:
    print_error(err)
    
print_title("Vector division - 3x1 / 2")

v1 = Vector([[8], [4], [2]])
n = 2

print_matrix(v1, name="v1", color=YELLOW)
try:
    ret = v1 / n
    print_matrix(ret, name="division")
    solution = Vector([[4], [2], [1]])
    print(GREEN + "OK" + RES) if isinstance(ret, Vector) else print(RED + "KO" + RES)
    print(GREEN + "OK" + RES) if ret.__eq__(solution) else print(RED + "KO" + RES)
except ValueError as err:
    print_error(err)
    
print_title("Vector scalar dot - 3x1 . 3x1")

v1 = Vector([[8], [4], [2]])
v2 = Vector([[1], [2], [3]])

print_matrix(v1, name="v1", color=YELLOW)
print_matrix(v2, name="v2", color=YELLOW)
try:
    ret = v1.dot(v2)
    solution = 22
    print(GREEN + "OK" + RES) if ret == solution else print(RED + "KO" + RES)
except ValueError as err:
    print_error(err)

print_title("Vector scalar dot - 1x3 . 1x3")

v1 = Vector([[8, 4, 2]])
v2 = Vector([[1, 2, 3]])

print_matrix(v1, name="v1", color=YELLOW)
print_matrix(v2, name="v2", color=YELLOW)
try:
    ret = v1.dot(v2)
    solution = 22
    print(GREEN + "OK" + RES) if ret == solution else print(RED + "KO" + RES)
except ValueError as err:
    print_error(err)

print_title("Subject main")

print("MY RESULT")
print(PINK + "EXPECTED", RES)
m1 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
print(m1.shape)
# Output:
print(PINK + "(3, 2)", RES)
print(m1.T().__str__())
# Output:
print(PINK + "Matrix([[0., 2., 4.], [1., 3., 5.]]", RES)
print(m1.T().shape)
# Output:
print(PINK + "(2, 3)", RES)
m1 = Matrix([[0., 2., 4.], [1., 3., 5.]])
print(m1.shape)
# Output:
print(PINK + "(2, 3)", RES)
print(m1.T().__str__())
# Output:
print(PINK + "Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]]", RES)
print(m1.T().shape)
# Output:
print(PINK + "(3, 2)", RES)
m1 = Matrix([[0.0, 1.0, 2.0, 3.0],
[0.0, 2.0, 4.0, 6.0]])
m2 = Matrix([[0.0, 1.0],
[2.0, 3.0],
[4.0, 5.0],
[6.0, 7.0]])
print((m1 * m2).__str__())
# Output:
print(PINK + "Matrix([[28., 34.], [56., 68.]]", RES)
m1 = Matrix([[0.0, 1.0, 2.0],
[0.0, 2.0, 4.0]])
v1 = Vector([[1], [2], [3]])
print((m1 * v1).__str__())
# Output:
print(PINK + "Matrix([[8], [16]]", RES)
# Or: Vector([[8], [16]
v1 = Vector([[1], [2], [3]])
v2 = Vector([[2], [4], [8]])
print((v1 + v2).__str__())
# Output:
print(PINK + "Vector([[3],[6],[11]]", RES)