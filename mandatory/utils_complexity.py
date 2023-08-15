import time
import random
from utils_colors import Colors
from class_matrix import Matrix
from class_vector import Vector
from utils_operations import reshape

def print_title(title, color=Colors.YELLOW):
    print(f"{color}{title}{Colors.RES}")

# def get_scalar_inputs(max_nb_digits=6):
#     tests_scalars = [10 ** i for i in range(max_nb_digits)]
#     return tests_scalars

def get_vector_inputs(max_nb_digits=6):
    tests_lists = [[random.randrange(0, 10) for _ in range(10 ** nb_elems)] for nb_elems in range(max_nb_digits)]
    tests_vectors = [Vector(*l) for l in tests_lists]
    return tests_vectors

def check_time_complexity(f, args, *extra_args):
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