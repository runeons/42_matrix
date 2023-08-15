from utils_colors import Colors
from class_matrix import Matrix
from class_vector import Vector
from utils_operations import reshape, matrix_from_shape, linear_combination
from utils_complexity import get_vector_inputs, check_time_complexity, get_matrix_inputs, check_time_complexity_vec_lin_comb
from utils_constants import *

def print_title(title, color=Colors.YELLOW):
    print(f"{color}{title}{Colors.RES}")

def main():
    try:
        vectors_1 = [
            Vector(1., 0., 0.),
            Vector(0., 1., 0.),
            Vector(0., 0., 1.),
        ]
        vectors_2 = [
            Vector(1., 2., 3.),
            Vector(0., 10., -100.),
        ]
        print_title(">>>>>>>>>> VECTOR linear combination <<<<<<<<<<", Colors.GREEN)
        linear_combination(vectors_1, [10., -2., 0.5]).summary()
        linear_combination(vectors_2, [10., -2.]).summary()

        if COMPLEXITY == True:
            # matrices_complexity_tests = get_matrix_inputs()
            check_time_complexity_vec_lin_comb(linear_combination)
            # check_time_complexity(linear_combination, matrices_complexity_tests, title="LINEAR COMBINATION MATRIX complexity")

    except ValueError as e:
        print(e)
if (__name__ == "__main__"):
    main()