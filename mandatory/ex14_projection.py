from utils_display import print_title
from bonus_projection import projection, to_file

def main():
    try:
        print_title(">>>>>>>>>> PROJECTION  <<<<<<<<<<")
        P = projection(100, 9/9, 10, 1000)
        P.summary()
        to_file(P)

    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()