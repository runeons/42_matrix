from class_vector import Vector
from utils_display import print_title, space_complexity
from utils_operations import linear_combination
from utils_complexity import time_complexity_vec_nums
from utils_constants import COMPLEXITY

def main():
    try:
        vectors_1 = [
            Vector(1., 0., 0.),
            Vector(0., 1., 0.),
            Vector(0., 0., 1.),
        ]
        vectors_2 = [
            Vector(1., 2., 3.),
            Vector(0., 10., -100.),
        ]
        print_title(">>>>>>>>>> VECTOR linear combination <<<<<<<<<<")
        linear_combination(vectors_1, [10., -2., 0.5]).summary()
        linear_combination(vectors_2, [10., -2.]).summary()

        if COMPLEXITY == True:
            time_complexity_vec_nums(space_complexity(linear_combination), "LINEAR COMBINATION VECTOR O(n)")

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()