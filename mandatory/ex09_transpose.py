from class_matrix import Matrix
from utils_display import print_title, print_OK, print_KO, space_complexity
from utils_complexity import time_complexity_mat
from utils_constants import COMPLEXITY

def evaluation_transpose():
    print_title(">>>>>>>>>> EVALUATION transpose <<<<<<<<<<")
    tests = [
        ([[0, 0], [0, 0]], [[0, 0], [0, 0]]),
        ([[1, 0], [0, 1]], [[1, 0], [0, 1]]),
        ([[1, 2], [3, 4]], [[1, 3], [2, 4]]),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
        ([[1, 2], [3, 4], [5, 6]], [[1, 3, 5], [2, 4, 6]])
    ]
    for t in tests:
        m1 = Matrix(t[0])
        res = m1.transpose()
        expected = Matrix(t[1])
        if (res == expected):   
            print_OK(f"{m1} transpose == {res} == {expected}")
        else:
            print_KO(f"{m1} transpose == {res} != {expected}")

def main():
    try:
        print_title(">>>>>>>>>> MATRIX transpose <<<<<<<<<<")
        Matrix([[1., 0. ], [0., 1. ]]).transpose().summary()
        Matrix([[1., 2. ], [3., 4. ]]).transpose().summary()
        Matrix([[2., -5., 0.], [4., 3., 7.], [-2., 3., 4.]]).transpose().summary()
        Matrix([[2., 0., -1.], [0., 3., 4.]]).transpose().summary()
        Matrix([[2., 3., 4.], [4., 6., 8.], [6., 9., 12.], [8., 12., 16.]]).transpose().summary()

        if COMPLEXITY == True:
            time_complexity_mat(space_complexity(Matrix.transpose), "MATRIX TRANSPOSE O(nm)")

        evaluation_transpose()

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()