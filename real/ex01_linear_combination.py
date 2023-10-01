from class_vector import Vector
from utils_display import print_title, print_OK, print_KO, space_complexity
from utils_operations import linear_combination
from utils_complexity import time_complexity_vec_nums
from utils_constants import COMPLEXITY

#   scale + addition
#   add vectors (1st param) scaled by 2nd param
#
# [10]  [-2  ]    (scale)      
# 
# (v1)  (v2)                            (res)
# [1]   [0   ]          10 + 0          [10 ]
# [2]   [10  ]          20 + -20        [0  ]              
# [3]   [-100]          30 + 200        [230]         
#

def evaluation_lc():
    print_title(">>>>>>>>>> EVALUATION linear combination <<<<<<<<<<")
    v_tests = [
        ([Vector([-42., 42.])], [-1.], [42., -42.]),
        ([Vector([-42.]), Vector([-42.]), Vector([-42.])], [-1., 1., 0.], [0.]),
        ([Vector([-42., 42.]), Vector([1., 3.]), Vector([10., 20.])], [1., -10., -1.], [-62., -8.]),
        ([Vector([-42., 100., -69.5]), Vector([1., 3., 5.])], [1., -10.], [-52., 70., -119.5])
    ]
    for t in v_tests:
        vectors = t[0]
        comb = t[1]
        expected = Vector(t[2])
        res = linear_combination(vectors, comb)
        if (res == expected):   
            print_OK(f"{res} == {expected}")
        else:
            print_KO(f"{res} != {expected}")

def main():
    try:
        vectors_1 = [
            Vector([1., 0., 0.]),
            Vector([0., 1., 0.]),
            Vector([0., 0., 1.]),
        ]
        vectors_2 = [
            Vector([1., 2., 3.]),
            Vector([0., 10., -100.]),
        ]
        comb_1 = [10., -2., 0.5]
        comb_2 = [10., -2.]
        expected_1 = Vector([10., -2., 0.5])
        expected_2 = Vector([10., 0., 230.])
        print_title(">>>>>>>>>> VECTOR linear combination <<<<<<<<<<")
        res_1 = linear_combination(vectors_1, comb_1)
        if (res_1 == expected_1):   
            print_OK(f"{res_1} == {expected_1}")
        else:
            print_KO(f"{res_1} != {expected_1}")
        res_2 = linear_combination(vectors_2, comb_2)
        if (res_2 == expected_2):   
            print_OK(f"{res_2} == {expected_2}")
        else:
            print_KO(f"{res_2} != {expected_2}")
    
        evaluation_lc()

        if COMPLEXITY == True:
            time_complexity_vec_nums(space_complexity(linear_combination), "LINEAR COMBINATION VECTOR O(n)")

    except ValueError as e:
        print(e)


if (__name__ == "__main__"):
    main()