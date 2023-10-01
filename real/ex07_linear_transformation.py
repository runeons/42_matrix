from class_vector import Vector
from class_matrix import Matrix
from utils_display import print_title, print_OK, print_KO, space_complexity
from utils_complexity import time_complexity_mat_vec, time_complexity_mat_mul
from utils_constants import COMPLEXITY

def evaluation_mat_vec_mult():
    print_title(">>>>>>>>>> EVALUATION multiplication <<<<<<<<<<")
    tests = [
      ([[0, 0], [0, 0]], [5, 7], [0, 0]),
      ([[1, 0], [0, 1]], [5, 7], [5, 7]),
      ([[1, 1], [1, 1]], [4, 2], [6, 6]),
      ([[2, 0], [0, 2]], [2, 1], [4, 2]),
      ([[0.5, 0], [0, 0.5]], [4, 2], [2, 1])
    ]
    for t in tests:
        m1 = Matrix(t[0])
        v1 = Vector(t[1])
        res = m1.mul_vec(v1)
        expected = Vector(t[2])
        if (res == expected):   
            print_OK(f"{m1} * {v1} == {res} == {expected}")
        else:
            print_KO(f"{m1} * {v1} == {res} != {expected}")

def main():
    try:
        print_title(">>>>>>>>>> MATRIX VECTOR multiplication <<<<<<<<<<")
        Matrix([[1., 0., ], [0., 1., ]]).mul_vec(Vector([4., 2.])).summary()
        Matrix([[1., 2., ], [3., 4., ], [5., 6., ]]).mul_vec(Vector([3., 2.])).summary()
        Matrix([[2., 0., ], [0., 2., ]]).mul_vec(Vector([4., 2.])).summary()
        Matrix([[2., -2., ], [-2, 2. ]]).mul_vec(Vector([4., 2.])).summary()

        print_title(">>>>>>>>>> MATRIX MATRIX multiplication <<<<<<<<<<")
        Matrix([[1., 0., ], [0., 1., ]]).mul_mat(Matrix([[1., 0., ], [0., 1., ]])).summary()
        Matrix([[1., 0., ], [0., 1., ]]).mul_mat(Matrix([[2., 1., ], [4., 2., ]])).summary()
        Matrix([[3., -5., ], [6., 8., ]]).mul_mat(Matrix([[2., 1., ], [4., 2., ]])).summary()

        if COMPLEXITY == True:
            time_complexity_mat_vec(space_complexity(Matrix.mul_vec), "MATRIX VECTOR MULTIPLICATION O(nm)") # matrix (m, n) * vector (n) => vector (m)
            time_complexity_mat_mul(space_complexity(Matrix.mul_mat), "MATRIX MATRIX MULTIPLICATION t:O(nmp) s:O(nm + mp + np)") # matrix (m, n) * matrix (n, p) => matrix (m, p)

        evaluation_mat_vec_mult()
    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()