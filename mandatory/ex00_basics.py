from utils_colors import Colors
from class_matrix import Matrix
from class_vector import Vector
from utils_operations import reshape

def print_title(title):
    print(f"{Colors.YELLOW}{title}{Colors.RES}")

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
        print_title("INSTANTIATE vector and matrix")
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

        print_title("RESHAPE vector and matrix")
        tests_reshape = [
            Matrix([1, 2, 3], [4, 5, 6]),
            Vector(2., 4.),
        ]
        for t in tests_reshape:
            print("---------------------")
            t.summary()
            reshape(t).summary()

        print_title("ADD two vectors")
        Vector(2., 3.).add(Vector(5., 7.)).summary()

        print_title("SUB two vectors")
        Vector(2., 3.).sub(Vector(5., 7.)).summary()

        print_title("SCALE vector")
        Vector(2., 3.).scl(2.).summary()

        # print_title("ADD two matrices")
        # Matrix([1., 2.], [3., 4.]).add(Matrix([7., 4.], [-2., 2])).summary()

        # print_title("SUB two matrices")
        # Matrix([1., 2.], [3., 4.]).sub(Matrix([7., 4.], [-2., 2])).summary()

        # print_title("SCALE matrix")
        # Matrix([1., 2.], [3., 4.]).scl(2.).summary()

    except ValueError as e:
        print(e)
if (__name__ == "__main__"):
    main()