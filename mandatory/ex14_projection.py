from utils_display import print_title
from bonus_projection import projection, to_file

def main():
    try:
        print_title(">>>>>>>>>> PROJECTION  <<<<<<<<<<")
        P = projection(90, 16/9, 1, 10) # fov, ratio, near, far
        # P = projection(160, 16/9, 1, 10) # fov, ratio, near, far
        # P = projection(90, 16/9, 1, 1000000) # fov, ratio, near, far
        # P = projection(90, 16/9, 10, 100) # fov, ratio, near, far
        P.summary()
        to_file(P)

    except FileNotFoundError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()