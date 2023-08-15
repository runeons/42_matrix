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

def get_coefs_inputs(max_nb_digits=MAX_NB_DIGITS):
    # tests_coefs = [vector_from_size(i + 1, fill_with=2) for i in range(max_nb_digits)]
    tests_coefs = [[2 for _ in range(i + 1)] for i in range(max_nb_digits)]
    return tests_coefs

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

def check_time_complexity(f, args, extra_args=None, title="Complexity"):
    if COMPLEXITY == False:
        return
    print_title(title)
    inputs = list(args)
    res = []
    for n in inputs:
        start_time = time.time_ns()
        if extra_args:
            f(n, extra_args)
        else:
            f(n, n)
        end_time = time.time_ns()
        execution_time = end_time - start_time
        res.append((n, execution_time))
    for i in range(0, len(res)):
        _, prev_time = res[i - 1]
        n, curr_time = res[i]
        if prev_time:
            ratio = curr_time / prev_time
            print(f"{Colors.BLUE}Size:{Colors.RES} {10 ** i}{Colors.BLUE}, Execution time: {Colors.RES}{curr_time}{Colors.BLUE}, Ratio: {Colors.RES}{ratio:.2f}")
        else:
            print(f"{Colors.BLUE}Size:{Colors.RES} {10 ** i}{Colors.BLUE}, Execution time: {Colors.RES}{curr_time}{Colors.BLUE}, Ratio: {Colors.RES}-")

def check_time_complexity_lin_comb(f, args, coefs, title="Complexity"):
    if COMPLEXITY == False:
        return
    print_title(title)
    inputs = args
    res = []
    for v, coef in zip(inputs, coefs):
        vectors = []
        for i in range(v.size()):
            vectors.append(v)           # create list of vectors to combinate, for each size (1, 10, 100...)
        start_time = time.time_ns()
        f(vectors, coef)
        end_time = time.time_ns()
        execution_time = end_time - start_time
        res.append((v.size(), execution_time))
    for i in range(0, len(res)):
        _, prev_time = res[i - 1]
        i, curr_time = res[i]
        if prev_time:
            ratio = curr_time / prev_time   # ^2 because v.size() AND len(vectors) increased each time
            print(f"{Colors.BLUE}Size:{Colors.RES} {i}^2{Colors.BLUE}, Execution time: {Colors.RES}{curr_time}{Colors.BLUE}, Ratio: {Colors.RES}{ratio:.2f}")
        else:
            print(f"{Colors.BLUE}Size:{Colors.RES} {i}^2{Colors.BLUE}, Execution time: {Colors.RES}{curr_time}{Colors.BLUE}, Ratio: {Colors.RES}-")