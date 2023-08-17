from class_matrix import Matrix
from utils_display import print_title, space_complexity
from utils_complexity import time_complexity_sq_mat_dim
from utils_constants import COMPLEXITY

def main():
    try:
        print_title(">>>>>>>>>> MATRIX determinant <<<<<<<<<<")
        print(Matrix([ 1., -1.], [-1., 1.]).determinant())
        print(Matrix([2., 0., 0.], [0., 2., 0.], [0., 0., 2.]).determinant())
        print(Matrix([8., 5., -2.], [4., 7., 20.], [7., 6., 1.]).determinant())
        print(Matrix([ 8., 5., -2., 4.], [ 4., 2.5, 20., 4.], [ 8., 5., 1., 4.], [28., -4., 17., 1.]).determinant())

        if COMPLEXITY == True:
            time_complexity_sq_mat_dim(space_complexity(Matrix.determinant), "MATRIX DETERMINANT", max_dim=4)

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()