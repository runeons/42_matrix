from class_matrix import Matrix
from utils_display import print_title
from utils_complexity import check_time_complexity_mat
from utils_constants import COMPLEXITY

def main():
    try:
        print_title(">>>>>>>>>> MATRIX determinant <<<<<<<<<<")
        Matrix([ 1., -1.], [-1., 1.]).determinant()
        Matrix([2., 0., 0.], [0., 2., 0.], [0., 0., 2.]).determinant()
        Matrix([8., 5., -2.], [4., 7., 20.], [7., 6., 1.]).determinant()
        Matrix([ 8., 5., -2., 4.], [ 4., 2.5, 20., 4.], [ 8., 5., 1., 4.], [28., -4., 17., 1.]).determinant()

        if COMPLEXITY == True:
            check_time_complexity_mat(Matrix.transpose, "MATRIX DETERMINANT")

    except ValueError as e:
        print(e)
if (__name__ == "__main__"):
    main()