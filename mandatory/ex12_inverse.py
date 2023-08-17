from class_matrix import Matrix
from utils_display import print_title
from utils_complexity import check_time_complexity_mat
from utils_constants import COMPLEXITY

def main():
    try:
        print_title(">>>>>>>>>> MATRIX inverse <<<<<<<<<<")
        Matrix([1., 0., 0.], [0., 1., 0.], [0., 0., 1.]).inverse().summary()
        Matrix([2., 0., 0.], [0., 2., 0.], [0., 0., 2.]).inverse().summary()
        Matrix([8., 5., -2.], [4., 7., 20.], [7., 6., 1.]).inverse().summary()

        if COMPLEXITY == True:
            check_time_complexity_mat(Matrix.inverse, "MATRIX INVERSE")

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()