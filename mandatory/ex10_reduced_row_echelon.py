from class_matrix import Matrix
from utils_display import print_title
from utils_complexity import time_complexity_mat
from utils_constants import COMPLEXITY

def main():
    try:
        print_title(">>>>>>>>>> MATRIX reduced row echelon <<<<<<<<<<")
        Matrix([1., 2. ], [3., 4. ]).row_echelon().summary()
        Matrix([1., 2. ], [2., 4. ]).row_echelon().summary()
        Matrix([0., 2. ], [0., 4. ]).row_echelon().summary()
        Matrix([8., 5., -2., 4., 28.], [4., 2.5, 20., 4., -4.], [8., 5., 1., 4., 17.]).row_echelon().summary()

        if COMPLEXITY == True:
            time_complexity_mat(Matrix.row_echelon, "MATRIX REDUCED ROW ECHELON")

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()