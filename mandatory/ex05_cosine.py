from class_vector import Vector
from utils_display import print_title, print_OK, print_KO, space_complexity
from utils_complexity import time_complexity_vec_vec
from utils_constants import COMPLEXITY
from utils_operations import angle_cos

def evaluation_cos():
    print_title(">>>>>>>>>> EVALUATION cosine <<<<<<<<<<")
    tests = [
        ([1, 0], [0, 1], 0),
        ([8, 7], [3, 2], 0.9914542955425437),
        ([1, 1], [1, 1], 1),
        ([4, 2], [1, 1], 0.9486832980505138),
        ([-7, 3], [6, 4], -0.5462677805469223),
    ]
    for t in tests:
        v1 = Vector(t[0])
        v2 = Vector(t[1])
        res = angle_cos(v1, v2)
        expected = t[2]
        if (res == expected):   
            print_OK(f"{v1} and {v2} cosine == {res} == {expected}")
        else:
            print_KO(f"{v1} and {v2} cosine == {res} != {expected}")

def main():
    try:
        print_title(">>>>>>>>>> VECTORS cosine <<<<<<<<<<")
        print(angle_cos(Vector([1., 0.]), Vector([1., 0.])))
        print(angle_cos(Vector([1., 0.]), Vector([0., 1.])))
        print(angle_cos(Vector([-1., 1.]), Vector([1., -1.])))
        print(angle_cos(Vector([2., 1.]), Vector([4., 2.])))
        print(angle_cos(Vector([1., 2., 3.]), Vector([4., 5., 6.])))

        if COMPLEXITY == True:
            time_complexity_vec_vec(space_complexity(angle_cos), "VECTORS COSINE O(n)")
        
        evaluation_cos()
        
    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()