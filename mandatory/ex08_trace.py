from class_matrix import Matrix
from utils_display import print_title, print_OK, print_KO
from utils_complexity import time_complexity_sq_mat
from utils_constants import COMPLEXITY

# somme de la diagonale principale d’une matrice carrée

def evaluation_trace():
    print_title(">>>>>>>>>> EVALUATION linear transform <<<<<<<<<<")
    tests = [
        ([[0, 0], [0, 0]], 0),
        ([[1, 0], [0, 1]], 2),
        ([[1, 2], [3, 4]], 5),
        ([[8, -7], [4, 2]], 10),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3)
    ]
    for t in tests:
        m1 = Matrix(t[0])
        res = m1.trace()
        expected = t[1]
        if (res == expected):   
            print_OK(f"{m1} trace == {res} == {expected}")
        else:
            print_KO(f"{m1} trace == {res} != {expected}")

def main():
    try:
        print_title(">>>>>>>>>> MATRIX trace <<<<<<<<<<")
        print(Matrix([[1., 0. ], [0., 1. ]]).trace())
        print(Matrix([[2., -5., 0.], [4., 3., 7.], [-2., 3., 4.]]).trace())
        print(Matrix([[-2., -8., 4.], [1., -23., 4.], [0., 6., 4.]]).trace())

        if COMPLEXITY == True:
            time_complexity_sq_mat(Matrix.trace, "MATRIX TRACE t:O(n)")

        evaluation_trace()

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()