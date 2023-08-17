from class_vector import Vector
from utils_display import print_title
from utils_complexity import check_time_complexity_vec_vec
from utils_constants import COMPLEXITY

def main():
    try:
        print_title(">>>>>>>>>> VECTOR dot product <<<<<<<<<<")
        print(Vector(0., 0.).dot(Vector(1., 1.)))
        print(Vector(1., 1.).dot(Vector(1., 1.)))
        print(Vector(-1., 6.).dot(Vector(3., 2.)))

        if COMPLEXITY == True:
            check_time_complexity_vec_vec(Vector.dot, "VECTOR dot product")

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()