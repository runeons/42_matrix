from class_matrix import Matrix
from utils_display import print_title
from utils_complexity import time_complexity_sq_mat
from utils_constants import COMPLEXITY

def main():
    try:
        print_title(">>>>>>>>>> MATRIX trace <<<<<<<<<<")
        print(Matrix([1., 0. ], [0., 1. ]).trace())
        print(Matrix([2., -5., 0.], [4., 3., 7.], [-2., 3., 4.]).trace())
        print(Matrix([-2., -8., 4.], [1., -23., 4.], [0., 6., 4.]).trace())

        if COMPLEXITY == True:
            time_complexity_sq_mat(Matrix.trace, "MATRIX TRACE t:O(n)")

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()