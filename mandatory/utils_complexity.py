import time
import random
from utils_colors import Colors
from utils_operations import matrix_from_shape, vector_from_size
from utils_constants import COMPLEXITY, MAX_NB_DIGITS, SIMPLE_VECTOR_SIZE, SIMPLE_SCALAR
from utils_display import print_title

def print_complexity_summary(res):
    for i in range(0, len(res)):
        n, curr_time = res[i]
        if (i == 0):
            print(f"{Colors.BLUE}Size:{Colors.RES} {n}{Colors.BLUE}, Execution time: {Colors.RES}{curr_time}{Colors.BLUE}, Ratio: {Colors.RES}-")
        else:
            _, prev_time = res[i - 1]
            ratio = curr_time / prev_time
            print(f"{Colors.BLUE}Size:{Colors.RES} {n}{Colors.BLUE}, Execution time: {Colors.RES}{curr_time}{Colors.BLUE}, Ratio: {Colors.RES}{ratio:.2f}")


def create_input_long_vector(complex_nb_digits):
    return vector_from_size(10 ** complex_nb_digits)

def create_input_long_matrix(complex_nb_digits):
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

def create_input_many_matrices(complex_nb_digits):
    x = y = 10 ** (int(complex_nb_digits / 2))
    if (complex_nb_digits % 2):
        y = y * 10
    return matrix_from_shape(x, y)

def create_input_many_numbers(complex_nb_digits):
    numbers = []
    for _ in range (10 ** complex_nb_digits):
        numbers.append(SIMPLE_SCALAR)
    return numbers

def check_time_complexity_vec_vec(f):
    if COMPLEXITY == False:
        return
    res = []
    for i in range(MAX_NB_DIGITS):
        v1 = create_input_long_vector(i)
        v2 = create_input_long_vector(i)
        start_time = time.time_ns()
        f(v1, v2)
        end_time = time.time_ns()
        execution_time = end_time - start_time
        res.append((10 ** i, execution_time))
    print_complexity_summary(res)
    
def check_time_complexity_mat_mat(f):
    if COMPLEXITY == False:
        return
    res = []
    for i in range(MAX_NB_DIGITS):
        m1 = create_input_long_matrix(i)
        m2 = create_input_long_matrix(i)
        start_time = time.time_ns()
        f(m1, m2)
        end_time = time.time_ns()
        execution_time = end_time - start_time
        res.append((10 ** i, execution_time))
    print_complexity_summary(res)

def check_time_complexity_vec_scal(f):
    if COMPLEXITY == False:
        return
    res = []
    for i in range(MAX_NB_DIGITS):
        v1 = create_input_long_vector(i)
        start_time = time.time_ns()
        f(v1, SIMPLE_SCALAR)
        end_time = time.time_ns()
        execution_time = end_time - start_time
        res.append((10 ** i, execution_time))
    print_complexity_summary(res)

def check_time_complexity_mat_scal(f):
    if COMPLEXITY == False:
        return
    res = []
    for i in range(MAX_NB_DIGITS):
        m1 = create_input_long_matrix(i)
        start_time = time.time_ns()
        f(m1, SIMPLE_SCALAR)
        end_time = time.time_ns()
        execution_time = end_time - start_time
        res.append((10 ** i, execution_time))
    print_complexity_summary(res)

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
    print_complexity_summary(res)

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
    print_complexity_summary(res)

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
    print_complexity_summary(res)

def check_time_complexity_vec(f, title):
    if COMPLEXITY == False:
        return
    print_title(title + " complexity")
    res = []
    for i in range(MAX_NB_DIGITS):
        v1 = create_input_long_vector(i)
        start_time = time.time_ns()
        f(v1)
        end_time = time.time_ns()
        execution_time = end_time - start_time
        res.append((10 ** i, execution_time))
    print_complexity_summary(res)
