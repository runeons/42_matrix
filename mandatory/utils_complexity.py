import time
import random
from utils_colors import Colors
from class_matrix import Matrix
from class_vector import Vector
from utils_operations import reshape, matrix_from_shape, vector_from_size
from utils_constants import *

def print_title(title, color=Colors.YELLOW):
    print(f"{color}{title}{Colors.RES}")

# def get_scalar_inputs(max_nb_digits=MAX_NB_DIGITS):
#     tests_scalars = [10 ** i for i in range(max_nb_digits)]
#     return tests_scalars

# def get_coefs_inputs(max_nb_digits=MAX_NB_DIGITS):
#     tests_coefs = [[2 for _ in range(i + 1)] for i in range(max_nb_digits)]
#     return tests_coefs

def get_vector_inputs(max_nb_digits=MAX_NB_DIGITS):
    tests_lists = [[float(random.randrange(0, 10)) for _ in range(10 ** nb_elems)] for nb_elems in range(max_nb_digits)]
    tests_vectors = [Vector(*l) for l in tests_lists]
    return tests_vectors

def get_matrix_inputs(max_nb_digits=MAX_NB_DIGITS):
    tests_matrices = []
    x = y = 1
    for it in range(max_nb_digits):
        if (it % 2):
            x = x * 10
        else:
            y = y * 10
        tests_matrices.append(matrix_from_shape(x, y))
    return tests_matrices

def create_input_long_matrix(complex_nb_digits):
    x = y = 10 ** (int(complex_nb_digits / 2))
    if (complex_nb_digits % 2):
        y = y * 10
    return matrix_from_shape(x, y)

def create_input_long_vector(complex_nb_digits):
    return vector_from_size(10 ** complex_nb_digits)

def create_input_many_matrices(complex_nb_digits):
    x = y = 10 ** (int(complex_nb_digits / 2))
    if (complex_nb_digits % 2):
        y = y * 10
    return matrix_from_shape(x, y)

def create_input_many_vectors(complex_nb_digits):
    simple_v = vector_from_size(SIMPLE_VECTOR_SIZE)
    vectors = []
    for _ in range (10 ** complex_nb_digits):
        vectors.append(simple_v)
    return vectors

def create_input_many_numbers(complex_nb_digits):
    numbers = []
    for _ in range (10 ** complex_nb_digits):
        numbers.append(SIMPLE_NUMBER)
    return numbers

def check_time_complexity(f, args, extra_args=None, title="Complexity"):
    if COMPLEXITY == False:
        return
    print_title(title)
    inputs = list(args)
    res = []
    for i, n in enumerate(inputs):
        start_time = time.time_ns()
        if extra_args:
            f(n, extra_args)
        else:
            f(n, n)
        end_time = time.time_ns()
        execution_time = end_time - start_time
        res.append((10 ** i, execution_time))
    for i in range(0, len(res)):
        n, curr_time = res[i]
        if (i == 0):
            print(f"{Colors.BLUE}Size:{Colors.RES} {n}{Colors.BLUE}, Execution time: {Colors.RES}{curr_time}{Colors.BLUE}, Ratio: {Colors.RES}-")
        else:
            _, prev_time = res[i - 1]
            ratio = curr_time / prev_time
            print(f"{Colors.BLUE}Size:{Colors.RES} {n}{Colors.BLUE}, Execution time: {Colors.RES}{curr_time}{Colors.BLUE}, Ratio: {Colors.RES}{ratio:.2f}")

def check_time_complexity_vec_nums(f):
    if COMPLEXITY == False:
        return
    print_title("LINEAR COMBINATION VECTOR complexity")
    res = []
    for i in range(MAX_NB_DIGITS):
        coefs = create_input_many_numbers(i)
        vectors = create_input_many_vectors(i)
        start_time = time.time_ns()
        f(vectors, coefs)
        end_time = time.time_ns()
        execution_time = end_time - start_time
        res.append((10 ** i, execution_time))
    for i in range(0, len(res)):
        n, curr_time = res[i]
        if (i == 0):
            print(f"{Colors.BLUE}Size:{Colors.RES} {n}{Colors.BLUE}, Execution time: {Colors.RES}{curr_time}{Colors.BLUE}, Ratio: {Colors.RES}-")
        else:
            _, prev_time = res[i - 1]
            ratio = curr_time / prev_time
            print(f"{Colors.BLUE}Size:{Colors.RES} {n}{Colors.BLUE}, Execution time: {Colors.RES}{curr_time}{Colors.BLUE}, Ratio: {Colors.RES}{ratio:.2f}")

def check_time_complexity_vec_vec_float(f):
    if COMPLEXITY == False:
        return
    print_title("LINEAR INTERPOLATION VECTOR complexity")
    res = []
    for i in range(MAX_NB_DIGITS):
        v1 = create_input_long_vector(i)
        v2 = create_input_long_vector(i)
        t = random.random()
        start_time = time.time_ns()
        f(v1, v2, t)
        end_time = time.time_ns()
        execution_time = end_time - start_time
        res.append((10 ** i, execution_time))
    for i in range(0, len(res)):
        n, curr_time = res[i]
        if (i == 0):
            print(f"{Colors.BLUE}Size:{Colors.RES} {n}{Colors.BLUE}, Execution time: {Colors.RES}{curr_time}{Colors.BLUE}, Ratio: {Colors.RES}-")
        else:
            _, prev_time = res[i - 1]
            ratio = curr_time / prev_time
            print(f"{Colors.BLUE}Size:{Colors.RES} {n}{Colors.BLUE}, Execution time: {Colors.RES}{curr_time}{Colors.BLUE}, Ratio: {Colors.RES}{ratio:.2f}")

def check_time_complexity_mat_mat_float(f):
    if COMPLEXITY == False:
        return
    print_title("LINEAR INTERPOLATION MATRIX complexity")
    res = []
    for i in range(MAX_NB_DIGITS):
        m1 = create_input_long_matrix(i)
        m2 = create_input_long_matrix(i)
        t = random.random()
        start_time = time.time_ns()
        f(m1, m2, t)
        end_time = time.time_ns()
        execution_time = end_time - start_time
        res.append((10 ** i, execution_time))
    for i in range(0, len(res)):
        n, curr_time = res[i]
        if (i == 0):
            print(f"{Colors.BLUE}Size:{Colors.RES} {n}{Colors.BLUE}, Execution time: {Colors.RES}{curr_time}{Colors.BLUE}, Ratio: {Colors.RES}-")
        else:
            _, prev_time = res[i - 1]
            ratio = curr_time / prev_time
            print(f"{Colors.BLUE}Size:{Colors.RES} {n}{Colors.BLUE}, Execution time: {Colors.RES}{curr_time}{Colors.BLUE}, Ratio: {Colors.RES}{ratio:.2f}")