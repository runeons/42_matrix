from utils_colors import Colors
from class_matrix import Matrix
from class_vector import Vector

def main():
    print(f"{Colors.YELLOW}TEST PRINT VECTOR/MATRIX{Colors.RES}")
    tests_print = [
        Vector(0., 1., 2.),
        Vector(2.,),
        Vector(),
        Vector(3.14, 2.71, 1.618),
        Vector(3.14, 2.71, 1.618, 3., 4., 5.),
        Vector("a", "b", "cde"),
        Matrix([1., 2.], [3., 4.]),
        Matrix([1, 2, 3], [4, 5, 6]),
        Matrix([7, 8], [9, 10], [11, 12]),
        Matrix(["a", "b", "c"], ["d", "e", "a"]),
        Matrix([]),
        Matrix([], []),
    ]
    for t in tests_print:
        print(t)

    print(f"{Colors.YELLOW}TEST VECTOR TO MATRIX{Colors.RES}")
    tests_vector = [
        Vector(2., 4.)
    ]
    for v in tests_vector:
        print(v)
        m = v.to_matrix()
        print(m)
if (__name__ == "__main__"):
    main()