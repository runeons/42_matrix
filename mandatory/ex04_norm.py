from class_vector import Vector
from utils_display import print_title, print_OK, print_KO, space_complexity
from utils_complexity import time_complexity_vec
from utils_constants import COMPLEXITY

def evaluation_euclidean_norm():
    print_title(">>>>>>>>>> EVALUATION Euclidean norm <<<<<<<<<<")
    tests = [
        ([0], 0),
        ([1], 1),
        ([0, 0], 0),
        ([1, 0], 1),
        ([2, 1], 2.236067977),
        ([4, 2], 4.472135955),
        ([-4, -2], 4.472135955)
    ]
    for t in tests:
        v1 = Vector(t[0])
        res = v1.norm()
        expected = t[1]
        if (res == expected):   
            print_OK(f"{v1} norm == {res} == {expected}")
        else:
            print_KO(f"{v1} norm == {res} != {expected}")


def evaluation_manhattan_norm():
    print_title(">>>>>>>>>> EVALUATION Euclidean norm <<<<<<<<<<")
    tests = [
        ([0], 0),
        ([1], 1),
        ([0, 0], 0),
        ([1, 0], 1),
        ([2, 1], 3),
        ([4, 2], 6),
        ([-4, -2], 6)
    ]
    for t in tests:
        v1 = Vector(t[0])
        res = v1.norm_1()
        expected = t[1]
        if (res == expected):   
            print_OK(f"{v1} norm == {res} == {expected}")
        else:
            print_KO(f"{v1} norm == {res} != {expected}")

def main():
    try:
        print_title(">>>>>>>>>> VECTOR norms <<<<<<<<<<")
        tests = [
            Vector([0., 0., 0.]),
            Vector([1., 2., 3.]),
            Vector([-1., -2.]),
        ]
        for v in tests:
            print(f"{v.norm_1()}, {v.norm()}, {v.norm_inf()}")

        if COMPLEXITY == True:
            time_complexity_vec(space_complexity(Vector.norm_1), "VECTOR NORM_1 O(n)")
            time_complexity_vec(space_complexity(Vector.norm), "VECTOR NORM_2 O(n)")
            time_complexity_vec(space_complexity(Vector.norm_inf), "VECTOR NORM_INF O(n)")

        evaluation_euclidean_norm()
        evaluation_manhattan_norm()

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()