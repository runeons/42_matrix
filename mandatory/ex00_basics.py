from utils_colors import Colors
from class_matrix import Matrix
from class_vector import Vector
from utils_operations import reshape
from utils_complexity import get_vector_inputs, check_time_complexity

def print_title(title, color=Colors.YELLOW):
    print(f"{color}{title}{Colors.RES}")

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
        print_title(">>>>>>>>>> INSTANTIATE vector and matrix <<<<<<<<<<")
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

        print_title(">>>>>>>>>> RESHAPE vector and matrix <<<<<<<<<<")
        tests_reshape = [
            Matrix([1, 2, 3], [4, 5, 6]),
            Vector(2., 4.),
        ]
        for t in tests_reshape:
            print("---------------------")
            t.summary()
            reshape(t).summary()

        print_title(">>>>>>>>>> OPERATIONS between vectors <<<<<<<<<<")
        print_title("tests vectors", Colors.GREEN)
        v1 = Vector(2., 3.)
        v2 = Vector(5., 7.)
        v1.summary()
        v2.summary()
        print_title("ADD two vectors")
        v1.add(v2).summary()
        print_title("SUB two vectors")
        v1.sub(v2).summary()
        print_title("SCALE vector")
        v1.scl(2.).summary()

        print_title(">>>>>>>>>> OPERATIONS between matrices <<<<<<<<<<")
        print_title("tests matrices", Colors.GREEN)
        m1 = Matrix([1., 2.], [3., 4.])
        m2 = Matrix([7., 4.], [-2., 2])
        m1.summary()
        m2.summary()
        print_title("ADD two matrices")
        m1.add(m2).summary()
        print_title("SUB two matrices")
        m1.sub(m2).summary()
        print_title("SCALE matrix")
        m1.scl(2.).summary()

        vectors_complexity_tests = get_vector_inputs()
        # scalars_complexity_tests = get_scalar_inputs()
        print_title("ADD VECTOR complexity")
        check_time_complexity(Vector.add, vectors_complexity_tests)
        print_title("SUB VECTOR complexity")
        check_time_complexity(Vector.sub, vectors_complexity_tests)
        print_title("SCL VECTOR complexity")
        check_time_complexity(Vector.scl, vectors_complexity_tests, 100)

    except ValueError as e:
        print(e)
if (__name__ == "__main__"):
    main()