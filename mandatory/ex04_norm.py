from class_vector import Vector
from utils_display import print_title, space_complexity
from utils_complexity import time_complexity_vec
from utils_constants import COMPLEXITY

def main():
    try:
        print_title(">>>>>>>>>> VECTOR norms <<<<<<<<<<")
        tests = [
            Vector(0., 0., 0.),
            Vector(1., 2., 3.),
            Vector(-1., -2.),
        ]
        for v in tests:
            print(f"{v.norm_1()}, {v.norm()}, {v.norm_inf()}")

        if COMPLEXITY == True:
            time_complexity_vec(space_complexity(Vector.norm_1), "VECTOR NORM_1")
            time_complexity_vec(space_complexity(Vector.norm), "VECTOR NORM_2")
            time_complexity_vec(space_complexity(Vector.norm_inf), "VECTOR NORM_INF")

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()