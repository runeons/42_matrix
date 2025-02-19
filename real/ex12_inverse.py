from class_matrix import Matrix, LogicError
from utils_display import print_title, print_OK, print_KO, space_complexity
from utils_complexity import time_complexity_sq_mat
from utils_constants import COMPLEXITY

def evaluation_inverse():
    print_title(">>>>>>>>>> EVALUATION inverse <<<<<<<<<<")
    tests = [
        ([[1, 0], [0, 1]], [[1, 0], [0, 1]]),
        ([[2, 0], [0, 2]], [[0.5, 0], [0, 0.5]]),
        ([[0.5, 0], [0, 0.5]], [[2, 0], [0, 2]]),
        ([[0, 1], [1, 0]], [[0, 1], [1, 0]]),
        ([[1, 2], [3, 4]], [[-2, 1], [1.5, -0.5]]),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
    ]
    for t in tests:
        m1 = Matrix(t[0])
        res = m1.inverse()
        expected = Matrix(t[1])
        if (res == expected):   
            print_OK(f"{m1} inverse == {res} == {expected}")
        else:
            print_KO(f"{m1} inverse == {res} != {expected}")

def main():
    try:
        print_title(">>>>>>>>>> MATRIX inverse <<<<<<<<<<")
        m_tests = [
            Matrix([[5.]]),
            Matrix([[1., 2.], [4., 6.]]), # res = [-3, 1], [2, -0.5]
            Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]),
            Matrix([[2., 0., 0.], [0., 2., 0.], [0., 0., 2.]]),
            Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.]])
        ]
        for m in m_tests:
            try:
                m.inverse().summary()
            except LogicError as e:
                print(e)

        evaluation_inverse()

        try:
            if COMPLEXITY == True:
                time_complexity_sq_mat(space_complexity(Matrix.inverse), "MATRIX INVERSE t:O(n^3) s:O(n^2)")
        except LogicError as e:
                print(e)

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()