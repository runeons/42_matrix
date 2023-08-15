from utils_colors import Colors
from class_vector import Vector
from class_matrix import Matrix
from utils_operations import linear_interpolation
from utils_complexity import check_time_complexity_vec_lin_comb
from utils_constants import *

def print_title(title, color=Colors.YELLOW):
    print(f"{color}{title}{Colors.RES}")

def main():
    try:
        int_tests = [
            (0., 1., 0.),
            (0., 1., 1.),
            (0., 1., 0.5),
            (21., 42., 0.3),
        ]
        print_title(">>>>>>>>>> INT linear combination <<<<<<<<<<", Colors.GREEN)
        for test in int_tests:
            print(linear_interpolation(*test))
        linear_interpolation(Vector(2., 1.), Vector(4., 2.), 0.3).summary()
        linear_interpolation(Matrix([2., 1.], [3., 4.]), Matrix([20., 10.], [30., 40.]), 0.5).summary()

        # if COMPLEXITY == True:
            # check_time_complexity_vec_lin_comb(linear_combination)

        # v1 = Vector(2., 1.)
        # v2 = Vector(4., 2.)
        # (v1 + v2).summary()
        # (v1 * 2).summary()

        # m1 = Matrix([2., 1.], [3., 4.])
        # m2 = Matrix([20., 10.], [30., 40.])
        # m1.summary()
        # (m1 + m2).summary()
        # (m1 * 3).summary()



    except ValueError as e:
        print(e)
if (__name__ == "__main__"):
    main()