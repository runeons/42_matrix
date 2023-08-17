from class_matrix import Matrix
from utils_display import print_title
from utils_complexity import check_time_complexity_mat
from utils_constants import COMPLEXITY

def main():
    try:
        print_title(">>>>>>>>>> MATRIX rank <<<<<<<<<<")
        print(Matrix([0., 1], [0., 1.]).rank()) # expect 1
        print(Matrix([1., 0., 0.], [0., 1., 0.], [0., 0., 1.]).rank())
        print(Matrix([ 1., 2., 0., 0.], [ 2., 4., 0., 0.], [-1., 2., 1., 1.]).rank())
        print(Matrix([ 8., 5., -2.], [ 4., 7., 20.], [ 7., 6., 1.], [21., 18., 7.]).rank())

        if COMPLEXITY == True:
            check_time_complexity_mat(Matrix.rank, "MATRIX RANK")

    except ValueError as e:
        print(e)
if (__name__ == "__main__"):
    main()