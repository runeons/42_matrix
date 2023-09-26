from utils_colors import Colors
from class_matrix import Matrix
from class_vector import Vector
from utils_display import print_title, print_OK, print_KO, space_complexity
from utils_operations import reshape, linear_combination
from utils_complexity import time_complexity_vec_vec, time_complexity_mat_mat, time_complexity_vec_scal, time_complexity_mat_scal
from utils_constants import COMPLEXITY
import numpy as np

def complex_add():
    print_title(">>>>>>>>>> COMPLEX add <<<<<<<<<<")
    v_tests = [
        ([5, 3], [4, 2]),
        ([5, 3, 2], [4, 2, 1]),
        ([3, 1], [-1, 2]),
    ]
    for t in v_tests:
        v1 = Vector(t[0])
        v2 = Vector(t[1])
        res = v1.add(v2)
        expected = np.array(v1.coordinates) + np.array(v2.coordinates)
        if (res == expected):   
            print_OK(f"{v1} + {v2} == {res} == {expected}")
        else:
            print_KO(f"{v1} + {v2} == {res} != {expected}")

    m_tests = [
        ([[1, 2], [3, 4]], [[2, 3], [4, 5]]),
    ]
    for t in m_tests:
        m1 = Matrix(t[0])
        m2 = Matrix(t[1])
        res = m1.add(m2)
        expected = np.array(m1.rows) + np.array(m2.rows)
        if (res == expected):   
            print_OK(f"{m1} + {m2} == {res} == {expected}")
        else:
            print_KO(f"{m1} + {m2} == {res} != {expected}")

def complex_sub():
    print_title(">>>>>>>>>> COMPLEX sub <<<<<<<<<<")
    v_tests = [
        ([-5, 6], [-8, 0]),
    ]
    for t in v_tests:
        v1 = Vector(t[0])
        v2 = Vector(t[1])
        expected = np.array(v1.coordinates) - np.array(v2.coordinates)
        res = v1.sub(v2)
        if (res == expected):   
            print_OK(f"{v1} - {v2} == {res} == {expected}")
        else:
            print_KO(f"{v1} - {v2} == {res} != {expected}")

    m_tests = [
        ([[1, 2], [3, 4]], [[2, 3], [4, 5]]),
    ]
    for t in m_tests:
        m1 = Matrix(t[0])
        m2 = Matrix(t[1])
        expected = np.array(m1.rows) - np.array(m2.rows)
        res = m1.sub(m2)
        if (res == expected):   
            print_OK(f"{m1} - {m2} == {res} == {expected}")
        else:
            print_KO(f"{m1} - {m2} == {res} != {expected}")

def complex_scl():
    print_title(">>>>>>>>>> COMPLEX scl <<<<<<<<<<")
    v_tests = [
        ([2, 4], 2),
    ]
    for t in v_tests:
        v1 = Vector(t[0])
        scalar = t[1]
        expected = np.array(v1.coordinates) * scalar
        res = v1.scl(scalar)
        if (res == expected):   
            print_OK(f"{v1} * {scalar} == {res} == {expected}")
        else:
            print_KO(f"{v1} * {scalar} == {res} != {expected}")

    m_tests = [
        ([[1, 2], [3, 4]], 2),
    ]
    for t in m_tests:
        m1 = Matrix(t[0])
        scalar = t[1]
        expected = np.array(m1.rows) * scalar
        res = m1.scl(scalar)
        if (res == expected):   
            print_OK(f"{m1} * {scalar} == {res} == {expected}")
        else:
            print_KO(f"{m1} * {scalar} == {res} != {expected}")

def complex_lc():
    print_title(">>>>>>>>>> COMPLEX linear combination <<<<<<<<<<")
    v_tests = [
        ([Vector([1., 2.]), Vector([1., 3.])], [4., 2.]),
    ]
    for t in v_tests:
        vectors = t[0]
        comb = t[1]
        expected = comb[0] * np.array(vectors[0].coordinates) + comb[1] * np.array(vectors[1].coordinates)
        res = linear_combination(vectors, comb)
        if (res == expected):   
            print_OK(f"{res} == {expected}")
        else:
            print_KO(f"{res} != {expected}")

def main():
    try:
        complex_add()
        complex_sub()
        complex_scl()
        complex_lc()

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()