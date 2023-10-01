from class_vector import Vector
from class_matrix import Matrix
from utils_display import print_title, print_OK, print_KO, space_complexity
from utils_operations import lerp
from utils_complexity import time_complexity_vec_vec_float, time_complexity_mat_mat_float
from utils_constants import COMPLEXITY

# trouve le point de l’espace entre les deux parametres (V/V ou M/M), au ratio t
# ex: lerp([1], [3], 0.5) = 2

# si plus de dimensions : entre les têtes de flèches

def evaluation_lerp():
    print_title(">>>>>>>>>> EVALUATION linear interpolation <<<<<<<<<<")
    tests = [
        ((0., 1., 0.), 0.),
        ((0., 1., 1.), 1.),
        ((0., 42., 0.5), 21.),
        ((-42., 42., 0.5), 0.),
        ((Vector([-42., 42.]), Vector([42., -42.]), 0.5), Vector([0., 0.]))
    ]
    for t in tests:
        res = lerp(t[0][0], t[0][1], t[0][2])
        expected = t[1]
        if (res == expected):   
            print_OK(f"lerp({t[0]})== {res} == {expected}")
        else:
            print_KO(f"lerp({t[0]})== {res} != {expected}")

def main():
    try:
        print_title(">>>>>>>>>> INT linear interpolation <<<<<<<<<<")
        int_tests = [
            (0., 1., 0.),
            (0., 1., 1.),
            (0., 1., 0.5),
            (21., 42., 0.3),
        ]
        for test in int_tests:
            print(lerp(*test))
        print_title(">>>>>>>>>> VECTOR linear interpolation <<<<<<<<<<")
        lerp(Vector([2., 1.]), Vector([4., 2.]), 0.3).summary()
        print_title(">>>>>>>>>> MATRIX linear interpolation <<<<<<<<<<")
        lerp(Matrix([[2., 1.], [3., 4.]]), Matrix([[20., 10.], [30., 40.]]), 0.5).summary()

        evaluation_lerp()

        if COMPLEXITY == True:
            time_complexity_vec_vec_float(space_complexity(lerp), "LINEAR INTERPOLATION VECTOR O(n)")
            time_complexity_mat_mat_float(space_complexity(lerp), "LINEAR INTERPOLATION MATRIX O(n)")

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()