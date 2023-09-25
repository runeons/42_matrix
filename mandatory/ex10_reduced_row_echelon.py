from class_matrix import Matrix
from utils_display import print_title, print_OK, print_KO, space_complexity
from utils_complexity import time_complexity_mat
from utils_constants import COMPLEXITY

def evaluation_row_echelon():
    print_title(">>>>>>>>>> EVALUATION row_echelon <<<<<<<<<<")
    tests = [
      ([[0, 0], [0, 0]], [[0, 0], [0, 0]]),
      ([[1, 0], [0, 1]], [[1, 0], [0, 1]]),
      ([[4, 2], [2, 1]], [[1, 0.5], [0, 0]]),
      ([[-7, 2], [4, 8]], [[1, 0], [0, 1]]),
      ([[1, 2], [4, 8]], [[1, 2], [0, 0]]),
    ]
    for t in tests:
        m1 = Matrix(t[0])
        res = m1.row_echelon()
        expected = Matrix(t[1])
        if (res == expected):   
            print_OK(f"{m1} row_echelon == {res} == {expected}")
        else:
            print_KO(f"{m1} row_echelon == {res} != {expected}")

def main():
    try:
        print_title(">>>>>>>>>> MATRIX partially reduced row echelon <<<<<<<<<<")
        Matrix([[1., 2. ], [3., 4. ]]).row_echelon().summary()
        Matrix([[1., 2. ], [2., 4. ]]).row_echelon().summary()
        Matrix([[0., 2. ], [0., 4. ]]).row_echelon().summary()
        Matrix([[8., 5., -2., 4., 28.], [4., 2.5, 20., 4., -4.], [8., 5., 1., 4., 17.]]).row_echelon().summary()

        if COMPLEXITY == True:
            time_complexity_mat(space_complexity(Matrix.row_echelon), "MATRIX PARTIALLY REDUCED ROW ECHELON t:O(n^3) s:O(n^2)")

        evaluation_row_echelon()

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()