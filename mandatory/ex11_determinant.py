from class_matrix import Matrix
from utils_display import print_title, print_OK, print_KO, space_complexity
from utils_complexity import time_complexity_sq_mat
from utils_constants import COMPLEXITY

# par combien l’aire du carré (volume du cube) est stretched or squeezed

def evaluation_determinant():
    print_title(">>>>>>>>>> EVALUATION determinant <<<<<<<<<<")
    tests = [
        ([[0, 0], [0, 0]], 0),
        ([[1, 0], [0, 1]], 1),
        ([[2, 0], [0, 2]], 4),
        ([[1, 1], [1, 1]], 0),
        ([[0, 1], [1, 0]], -1),
        ([[1, 2], [3, 4]], -2),
        ([[-7, 5], [4, 6]], -62),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 1),
    ]
    for t in tests:
        m1 = Matrix(t[0])
        res = m1.determinant()
        expected = t[1]
        if (res == expected):   
            print_OK(f"{m1} determinant == {res} == {expected}")
        else:
            print_KO(f"{m1} determinant == {res} != {expected}")

def main():
    try:
        print_title(">>>>>>>>>> MATRIX determinant <<<<<<<<<<")
        print(Matrix([[ 3.]]).determinant())
        print(Matrix([[ 1., 2.], [3., 4.]]).determinant())
        print(Matrix([[ 1., -1.], [-1., 1.]]).determinant())
        print(Matrix([[0., 2., 0., 0.], [0., 0., 2., 0.], [0., 0., 0., 2.], [0., 0., 0., 2.]]).determinant())
        print(Matrix([[2., 0., 0.], [0., 2., 0.], [0., 0., 2.]]).determinant())
        print(Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.]]).determinant())
        print(Matrix([[ 8., 5., -2., 4.], [ 4., 2.5, 20., 4.], [ 8., 5., 1., 4.], [28., -4., 17., 1.]]).determinant())

        evaluation_determinant()

        if COMPLEXITY == True:
            time_complexity_sq_mat(space_complexity(Matrix.determinant), "MATRIX DETERMINANT t:O(n^3) s:O(n^2)")

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()