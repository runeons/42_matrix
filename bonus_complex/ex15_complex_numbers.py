from utils_colors import Colors
from class_matrix import Matrix
from class_vector import Vector
from utils_display import print_title, print_OK, print_KO, space_complexity
from utils_operations import reshape
from utils_complexity import time_complexity_vec_vec, time_complexity_mat_mat, time_complexity_vec_scal, time_complexity_mat_scal
from utils_constants import COMPLEXITY

def complex_add():
    print_title(">>>>>>>>>> COMPLEX add <<<<<<<<<<")
    v_tests = [
        (([5, 3], [4, 2]), [9, 5]),
        (([3, 1], [-1, 2]), [2, 3]),
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
        (([[1, 2], [3, 4]], [[2, 3], [4, 5]]), [[3, 5], [7, 9]]),
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

def complex_sub():
    print_title(">>>>>>>>>> COMPLEX sub <<<<<<<<<<")
    v_tests = [
        (([-5, 6], [-8, 0]), [3, 6]),
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
        (([[1, 2], [3, 4]], [[2, 3], [4, 5]]), [[-1, -1], [-1, -1]]),
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


def complex_scl():
    print_title(">>>>>>>>>> COMPLEX scl <<<<<<<<<<")
    v_tests = [
        (([2, 4], 2), [4, 8]),
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
        (([[1, 2], [3, 4]], 2), [[2, 4], [6, 8]]),
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
        complex_add()
        complex_sub()
        complex_scl()

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()