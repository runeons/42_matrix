from class_vector import Vector
from class_matrix import Matrix
from utils_display import print_title
from utils_operations import lerp
from utils_complexity import check_time_complexity_vec_vec_float, check_time_complexity_mat_mat_float
from utils_constants import COMPLEXITY

def main():
    try:
        print_title(">>>>>>>>>> INT linear interpolation <<<<<<<<<<")
        int_tests = [
            (0., 1., 0.),
            (0., 1., 1.),
            (0., 1., 0.5),
            (21., 42., 0.3),
        ]
        for test in int_tests:
            print(lerp(*test))
        print_title(">>>>>>>>>> VECTOR linear interpolation <<<<<<<<<<")
        lerp(Vector(2., 1.), Vector(4., 2.), 0.3).summary()
        print_title(">>>>>>>>>> MATRIX linear interpolation <<<<<<<<<<")
        lerp(Matrix([2., 1.], [3., 4.]), Matrix([20., 10.], [30., 40.]), 0.5).summary()

        if COMPLEXITY == True:
            check_time_complexity_vec_vec_float(lerp, "LINEAR INTERPOLATION VECTOR")
            check_time_complexity_mat_mat_float(lerp, "LINEAR INTERPOLATION MATRIX")

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()