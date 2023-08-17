from class_vector import Vector
from utils_display import print_title
from utils_complexity import time_complexity_vec_vec
from utils_constants import COMPLEXITY
from utils_operations import angle_cos

def main():
    try:
        print_title(">>>>>>>>>> VECTORS cosine <<<<<<<<<<")
        print(angle_cos(Vector(1., 0.), Vector(1., 0.)))
        print(angle_cos(Vector(1., 0.), Vector(0., 1.)))
        print(angle_cos(Vector(-1., 1.), Vector(1., -1.)))
        print(angle_cos(Vector(2., 1.), Vector(4., 2.)))
        print(angle_cos(Vector(1., 2., 3.), Vector(4., 5., 6.)))

        if COMPLEXITY == True:
            time_complexity_vec_vec(angle_cos, "VECTORS COSINE")

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()