from class_vector import Vector
from utils_display import print_title, print_OK, print_KO, space_complexity
from utils_complexity import time_complexity_vec_vec
from utils_constants import COMPLEXITY

# histoire de projection
# très utile, comme pour déterminer si 2 vecteurs pointent dans la même direction (si dot > 0)
# **il permet aussi au vecteur de réaliser son rêve et entrer dans le monde des matrices, des transformations**

def evaluation_dot():
    print_title(">>>>>>>>>> EVALUATION dot product <<<<<<<<<<")
    tests = [
        (([0, 0], [0, 0]), 0),
        (([1, 0], [0, 0]), 0),
        (([1, 0], [1, 0]), 1),
        (([1, 0], [0, 1]), 0),
        (([1, 1], [1, 1]), 2),
        (([4, 2], [2, 1]), 10)
    ]
    for t in tests:
        v1 = Vector(t[0][0])
        v2 = Vector(t[0][1])
        expected = t[1]
        res = v1.dot(v2)
        if (res == expected):   
            print_OK(f"{v1} dot {v2} == {res} == {expected}")
        else:
            print_KO(f"{v1} dot {v2} == {res} != {expected}")


def main():
    try:
        print_title(">>>>>>>>>> VECTOR dot product <<<<<<<<<<")
        print(Vector([0., 0.]).dot(Vector([1., 1.])))
        print(Vector([1., 1.]).dot(Vector([1., 1.])))
        print(Vector([-1., 6.]).dot(Vector([3., 2.])))

        evaluation_dot()

        if COMPLEXITY == True:
            time_complexity_vec_vec(space_complexity(Vector.dot), "VECTOR dot product O(n)")

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()