from class_matrix import Matrix
from utils_display import print_title
from utils_complexity import check_time_complexity_mat
from utils_constants import COMPLEXITY

def main():
    try:
        print_title(">>>>>>>>>> MATRIX transpose <<<<<<<<<<")
        Matrix([1., 0. ], [0., 1. ]).transpose().summary()
        Matrix([1., 2. ], [3., 4. ]).transpose().summary()
        Matrix([2., -5., 0.], [4., 3., 7.], [-2., 3., 4.]).transpose().summary()
        Matrix([2., 0., -1.], [0., 3., 4.]).transpose().summary()
        Matrix([2., 3., 4.], [4., 6., 8.], [6., 9., 12.], [8., 12., 16.]).transpose().summary()

        if COMPLEXITY == True:
            check_time_complexity_mat(Matrix.transpose, "MATRIX TRANSPOSE")

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()