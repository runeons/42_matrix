from class_vector import Vector
from utils_display import print_title, print_OK, print_KO
from utils_operations import cross_product

# Vecteur orthogonal au plan qui est constitué par les deux vecteurs initiaux
# sa longueur = l’aire du parallélogramme compris entre les deux premiers vecteurs

def evaluation_cross():
    print_title(">>>>>>>>>> EVALUATION cross product <<<<<<<<<<")
    tests = [
        ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
        ([1, 0, 0], [0, 0, 0], [0, 0, 0]),
        ([1, 0, 0], [0, 1, 0], [0, 0, 1]),
        ([8, 7, -4], [3, 2, 1], [15, -20, -5]),
        ([1, 1, 1], [0, 0, 0], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0])
    ]
    for t in tests:
        v1 = Vector(t[0])
        v2 = Vector(t[1])
        res = cross_product(v1, v2)
        expected = Vector(t[2])
        if (res == expected):   
            print_OK(f"{v1} norm == {res} == {expected}")
        else:
            print_KO(f"{v1} norm == {res} != {expected}")

def main():
    try:
        print_title(">>>>>>>>>> VECTORS cross product <<<<<<<<<<")
        print(cross_product(Vector([0., 0., 1.]), Vector([1., 0., 0.])))
        print(cross_product(Vector([1., 2., 3.]), Vector([4., 5., 6.])))
        print(cross_product(Vector([4., 2., -3.]), Vector([-2., -5., 16.])))

        evaluation_cross()

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()