from utils_colors import Colors
from class_matrix import Matrix
from class_vector import Vector
from utils_display import print_title, print_OK, print_KO, space_complexity
from utils_operations import reshape
from utils_complexity import time_complexity_vec_vec, time_complexity_mat_mat, time_complexity_vec_scal, time_complexity_mat_scal
from utils_constants import COMPLEXITY

def evaluation_add():
    print_title(">>>>>>>>>> EVALUATION add <<<<<<<<<<")
    v_tests = [
        (([0, 0], [0, 0]), [0, 0]),
        (([1, 0], [0, 1]), [1, 1]),
        (([1, 1], [1, 1]), [2, 2]),
        (([21, 21], [21, 21]), [42, 42]),
        (([-21, 21], [21, -21]), [0, 0]),
        (([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]),
    ]
    for t in v_tests:
        v1 = Vector(t[0][0])
        v2 = Vector(t[0][1])
        expected = Vector(t[1])
        res = v1.add(v2)
        if (res == expected):   
            print_OK(f"{v1} + {v2} == {res} == {expected}")
        else:
            print_KO(f"{v1} + {v2} == {res} != {expected}")

    m_tests = [
        (([[0, 0], [0, 0]], [[0, 0], [0, 0]]), [[0, 0], [0, 0]]),
        (([[1, 0], [0, 1]], [[0, 0], [0, 0]]), [[1, 0], [0, 1]]),
        (([[1, 1], [1, 1]], [[1, 1], [1, 1]]), [[2, 2], [2, 2]]),
        (([[21, 21], [21, 21]], [[21, 21], [21, 21]]), [[42, 42], [42, 42]]),
    ]
    for t in m_tests:
        m1 = Matrix(t[0][0])
        m2 = Matrix(t[0][1])
        expected = Matrix(t[1])
        res = m1.add(m2)
        if (res == expected):   
            print_OK(f"{m1} + {m2} == {res} == {expected}")
        else:
            print_KO(f"{m1} + {m2} == {res} != {expected}")

def evaluation_sub():
    print_title(">>>>>>>>>> EVALUATION sub <<<<<<<<<<")
    v_tests = [
        (([0, 0], [0, 0]), [0, 0]),
        (([1, 0], [0, 1]), [1, -1]),
        (([1, 1], [1, 1]), [0, 0]),
        (([21, 21], [21, 21]), [0, 0]),
        (([-21, 21], [21, -21]), [-42, 42]),
        (([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9]),
    ]
    for t in v_tests:
        v1 = Vector(t[0][0])
        v2 = Vector(t[0][1])
        expected = Vector(t[1])
        res = v1.sub(v2)
        if (res == expected):   
            print_OK(f"{v1} - {v2} == {res} == {expected}")
        else:
            print_KO(f"{v1} - {v2} == {res} != {expected}")

    m_tests = [
        (([[0, 0], [0, 0]], [[0, 0], [0, 0]]), [[0, 0], [0, 0]]),
        (([[1, 0], [0, 1]], [[0, 0], [0, 0]]), [[1, 0], [0, 1]]),
        (([[1, 1], [1, 1]], [[1, 1], [1, 1]]), [[0, 0], [0, 0]]),
        (([[21, 21], [21, 21]], [[21, 21], [21, 21]]), [[0, 0], [0, 0]]),
    ]
    for t in m_tests:
        m1 = Matrix(t[0][0])
        m2 = Matrix(t[0][1])
        expected = Matrix(t[1])
        res = m1.sub(m2)
        if (res == expected):   
            print_OK(f"{m1} - {m2} == {res} == {expected}")
        else:
            print_KO(f"{m1} - {m2} == {res} != {expected}")


def evaluation_scl():
    print_title(">>>>>>>>>> EVALUATION scl <<<<<<<<<<")
    v_tests = [
        (([0, 0], 1), [0, 0]),
        (([1, 0], 1), [1, 0]),
        (([1, 1], 2), [2, 2]),
        (([21, 21], 2), [42, 42]),
        (([42, 42], 0.5), [21, 21]),
    ]
    for t in v_tests:
        v1 = Vector(t[0][0])
        scalar = t[0][1]
        expected = Vector(t[1])
        res = v1.scl(scalar)
        if (res == expected):   
            print_OK(f"{v1} * {scalar} == {res} == {expected}")
        else:
            print_KO(f"{v1} * {scalar} == {res} != {expected}")

    m_tests = [
        (([[0, 0], [0, 0]], 0), [[0, 0], [0, 0]]),
        (([[1, 0], [0, 1]], 1), [[1, 0], [0, 1]]),
        (([[1, 2], [3, 4]], 2), [[2, 4], [6, 8]]),
        (([[21, 21], [21, 21]], 0.5), [[10.5, 10.5], [10.5, 10.5]]),
    ]
    for t in m_tests:
        m1 = Matrix(t[0][0])
        scalar = t[0][1]
        expected = Matrix(t[1])
        res = m1.scl(scalar)
        if (res == expected):   
            print_OK(f"{m1} * {scalar} == {res} == {expected}")
        else:
            print_KO(f"{m1} * {scalar} == {res} != {expected}")

def main():
    try:
        tests_not_valid = [
            # Vector(),
            # Vector([]),
            # Matrix([1]),
            # Matrix([["a", "b", "c"], ["d", "e", "a"]]),
            # Matrix([["a"], ["d", "e"]]),
            # Matrix([["a", "b", "c"], ["d", "e"]]),
            # Matrix([[]]),
            # Matrix([[], []]),
        ]
        print_title(">>>>>>>>>> INSTANTIATE vector and matrix <<<<<<<<<<")
        tests_print = [
            Vector([0., 1., 2.]),
            Vector([2.,]),
            Vector([3.14, 2.71, 1.618]),
            Vector([3.14, 2.71, 1.618, 3., 4., 5.]),
            Vector(["a", "b", "cde"]),
            Matrix([[1., 2.], [3., 4.]]),
            Matrix([[1, 2, 3], [4, 5, 6]]),
            Matrix([[7, 8], [9, 10], [11, 12]]),
            Matrix([[1]]),
        ]
        for t in tests_print:
            print("---------------------")
            t.summary()

        print_title(">>>>>>>>>> RESHAPE vector and matrix <<<<<<<<<<")
        tests_reshape = [
            Matrix([[1, 2, 3], [4, 5, 6]]),
            Vector([2., 4.]),
        ]
        for t in tests_reshape:
            print("---------------------")
            t.summary()
            reshape(t).summary()

        print_title(">>>>>>>>>> OPERATIONS between vectors <<<<<<<<<<")
        print_title("tests vectors", Colors.GREEN)
        v1 = Vector([2., 3.])
        v2 = Vector([5., 7.])
        v1.summary()
        v2.summary()
        print_title(f"ADD two vectors: {v1} + {v2}")
        v1.add(v2).summary()
        print_title(f"SUB two vectors: {v1} + {v2}")
        v1.sub(v2).summary()
        print_title(f"SCALE vector: {v1} * 2")
        v1.scl(2.).summary()

        print_title(">>>>>>>>>> OPERATIONS between matrices <<<<<<<<<<")
        print_title("tests matrices", Colors.GREEN)
        m1 = Matrix([[1., 2.], [3., 4.]])
        m2 = Matrix([[7., 4.], [-2., 2]])
        m1.summary()
        m2.summary()
        print_title(f"ADD two matrices: {m1} + {m2}")
        m1.add(m2).summary()
        print_title(f"SUB two matrices: {m1} + {m2}")
        m1.sub(m2).summary()
        print_title(f"SCALE matrix: {m1} * 2")
        m1.scl(2.).summary()

        evaluation_add()
        evaluation_sub()
        evaluation_scl()

        if COMPLEXITY == True:
            print_title(">>>>>>>>>> BASIC OPERATIONS complexity <<<<<<<<<<")
            time_complexity_vec_vec(space_complexity(Vector.add), "ADD VECTOR O(n)")
            time_complexity_vec_vec(space_complexity(Vector.sub), "SUB VECTOR O(n)")
            time_complexity_vec_scal(space_complexity(Vector.scl), "SCL VECTOR O(n)")
            time_complexity_mat_mat(space_complexity(Matrix.add), "ADD MATRIX O(n)")
            time_complexity_mat_mat(space_complexity(Matrix.sub), "SUB MATRIX O(n)")
            time_complexity_mat_scal(space_complexity(Matrix.scl), "SCL MATRIX O(n)")

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()