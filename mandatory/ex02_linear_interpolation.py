from utils_colors import Colors
from class_vector import Vector
from class_matrix import Matrix
from utils_operations import lerp
from utils_complexity import check_time_complexity_vec_vec_float, check_time_complexity_mat_mat_float
from utils_constants import *

def print_title(title, color=Colors.YELLOW):
    print(f"{color}{title}{Colors.RES}")

def main():
    try:
        print_title(">>>>>>>>>> INT linear interpolation <<<<<<<<<<", Colors.GREEN)
        int_tests = [
            (0., 1., 0.),
            (0., 1., 1.),
            (0., 1., 0.5),
            (21., 42., 0.3),
        ]
        for test in int_tests:
            print(lerp(*test))
        print_title(">>>>>>>>>> VECTOR linear interpolation <<<<<<<<<<", Colors.GREEN)
        lerp(Vector(2., 1.), Vector(4., 2.), 0.3).summary()
        print_title(">>>>>>>>>> MATRIX linear interpolation <<<<<<<<<<", Colors.GREEN)
        lerp(Matrix([2., 1.], [3., 4.]), Matrix([20., 10.], [30., 40.]), 0.5).summary()

        if COMPLEXITY == True:
            check_time_complexity_vec_vec_float(lerp)
            check_time_complexity_mat_mat_float(lerp)

    except ValueError as e:
        print(e)
if (__name__ == "__main__"):
    main()