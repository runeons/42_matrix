from utils_display import print_title
from bonus_projection import projection, to_file

def main():
    try:
        print_title(">>>>>>>>>> PROJECTION  <<<<<<<<<<")
        P = projection(90, 9/9, 10, 10000) # ratio
        P.summary()
        to_file(P)

    except ValueError as e:
        print(e)

if (__name__ == "__main__"):
    main()