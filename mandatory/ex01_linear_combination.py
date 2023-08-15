from utils_colors import Colors
from class_vector import Vector
from utils_operations import linear_combination
from utils_complexity import check_time_complexity_vec_nums
from utils_constants import *

def print_title(title, color=Colors.YELLOW):
    print(f"{color}{title}{Colors.RES}")

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
        print_title(">>>>>>>>>> VECTOR linear combination <<<<<<<<<<", Colors.GREEN)
        linear_combination(vectors_1, [10., -2., 0.5]).summary()
        linear_combination(vectors_2, [10., -2.]).summary()

        if COMPLEXITY == True:
            check_time_complexity_vec_nums(linear_combination)

    except ValueError as e:
        print(e)
if (__name__ == "__main__"):
    main()