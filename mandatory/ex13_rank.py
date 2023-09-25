from class_matrix import Matrix
from utils_display import print_title, print_OK, print_KO
from utils_complexity import time_complexity_mat
from utils_constants import COMPLEXITY

# c’est le nombre de dimensions après transformation

def evaluation_inverse():
    print_title(">>>>>>>>>> EVALUATION rank <<<<<<<<<<")
    tests = [
        ([[0, 0], [0, 0]], 0),
        ([[1, 0], [0, 1]], 2),
        ([[2, 0], [0, 2]], 2),
        ([[1, 1], [1, 1]], 1),
        ([[0, 1], [1, 0]], 2),
        ([[1, 2], [3, 4]], 2),
        ([[-7, 5], [4, 6]], 2),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
    ]
    for t in tests:
        m1 = Matrix(t[0])
        res = m1.rank()
        expected = t[1]
        if (res == expected):   
            print_OK(f"{m1} rank == {res} == {expected}")
        else:
            print_KO(f"{m1} rank == {res} != {expected}")

def main():
    try:
        print_title(">>>>>>>>>> MATRIX rank <<<<<<<<<<")
        print(Matrix([[0., 1], [0., 1.]]).rank()) # expect 1
        print(Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]).rank())
        print(Matrix([[ 1., 2., 0., 0.], [ 2., 4., 0., 0.], [-1., 2., 1., 1.]]).rank())
        print(Matrix([[ 8., 5., -2.], [ 4., 7., 20.], [ 7., 6., 1.], [21., 18., 7.]]).rank())

        evaluation_inverse()
        
        if COMPLEXITY == True:
            time_complexity_mat(Matrix.rank, "MATRIX RANK t:O(n^3)")

    except ValueError as e:
        print(e)
if (__name__ == "__main__"):
    main()