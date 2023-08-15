from class_vector import Vector
from utils_display import print_title
from utils_operations import cross_product

def main():
    try:
        print_title(">>>>>>>>>> VECTORS cross product <<<<<<<<<<")
        print(cross_product(Vector(0., 0., 1.), Vector(1., 0., 0.)))
        print(cross_product(Vector(1., 2., 3.), Vector(4., 5., 6.)))
        print(cross_product(Vector(4., 2., -3.), Vector(-2., -5., 16.)))

    except ValueError as e:
        print(e)
if (__name__ == "__main__"):
    main()