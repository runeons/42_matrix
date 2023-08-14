from utils_colors import Colors
from class_matrix import Matrix
from class_vector import Vector
from utils_operations import reshape

def main():
    try:
        tests_not_valid = [
            # Vector(),
            # Matrix(1),
            # Matrix(["a", "b", "c"], ["d", "e", "a"]),
            # Matrix(["a"], ["d", "e"]),
            # Matrix(["a", "b", "c"], ["d", "e"]),
            # Matrix([]),
            # Matrix([], []),
        ]
        print(f"{Colors.YELLOW}INSTANTIATE vector and matrix{Colors.RES}")
        tests_print = [
            Vector(0., 1., 2.),
            Vector(2.,),
            Vector(3.14, 2.71, 1.618),
            Vector(3.14, 2.71, 1.618, 3., 4., 5.),
            Vector("a", "b", "cde"),
            Matrix([1., 2.], [3., 4.]),
            Matrix([1, 2, 3], [4, 5, 6]),
            Matrix([7, 8], [9, 10], [11, 12]),
            Matrix([1]),
        ]
        for t in tests_print:
            print("---------------------")
            t.summary()

        print(f"{Colors.YELLOW}RESHAPE vector and matrix{Colors.RES}")
        tests_reshape = [
            Matrix([1, 2, 3], [4, 5, 6]),
            Vector(2., 4.),
        ]
        for t in tests_reshape:
            print("---------------------")
            t.summary()
            reshape(t).summary()

    except ValueError as e:
        print(e)
if (__name__ == "__main__"):
    main()