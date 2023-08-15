from utils_colors import Colors
from class_vector import Vector
from class_matrix import Matrix
from utils_operations import lerp
from utils_complexity import check_time_complexity_lerp_vec, check_time_complexity_lerp_mat
from utils_constants import *

def print_title(title, color=Colors.YELLOW):
    print(f"{color}{title}{Colors.RES}")

def main():
    try:
        print_title(">>>>>>>>>> VECTOR dot product <<<<<<<<<<", Colors.GREEN)
        print(Vector(0., 0.).dot(Vector(1., 1.)))
        print(Vector(1., 1.).dot(Vector(1., 1.)))
        print(Vector(-1., 6.).dot(Vector(3., 2.)))

        # if COMPLEXITY == True:
        #     check_time_complexity_lerp_vec(lerp)
        #     check_time_complexity_lerp_mat(lerp)

    except ValueError as e:
        print(e)
if (__name__ == "__main__"):
    main()