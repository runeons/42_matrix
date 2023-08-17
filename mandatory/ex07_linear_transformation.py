from class_vector import Vector
from class_matrix import Matrix
from utils_display import print_title
from utils_complexity import time_complexity_mat_vec, time_complexity_mat_mul
from utils_constants import COMPLEXITY

def main():
    try:
        print_title(">>>>>>>>>> MATRIX VECTOR multiplication <<<<<<<<<<")
        Matrix([1., 0., ], [0., 1., ]).mul_vec(Vector(4., 2.)).summary()
        Matrix([2., 0., ], [0., 2., ]).mul_vec(Vector(4., 2.)).summary()
        Matrix([2., -2., ], [-2, 2. ]).mul_vec(Vector(4., 2.)).summary()

        print_title(">>>>>>>>>> MATRIX MATRIX multiplication <<<<<<<<<<")
        Matrix([1., 0., ], [0., 1., ]).mul_mat(Matrix([1., 0., ], [0., 1., ])).summary()
        Matrix([1., 0., ], [0., 1., ]).mul_mat(Matrix([2., 1., ], [4., 2., ])).summary()
        Matrix([3., -5., ], [6., 8., ]).mul_mat(Matrix([2., 1., ], [4., 2., ])).summary()

        if COMPLEXITY == True:
            time_complexity_mat_vec(Matrix.mul_vec, "MATRIX VECTOR MULTIPLICATION")
            time_complexity_mat_mul(Matrix.mul_mat, "MATRIX MATRIX MULTIPLICATION")

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()