import numpy as np
from termcolor import colored

def missing_vector_magnitude(missing_vector_x, missing_vector_y):
    missing_vector_magnitude = np.sqrt((missing_vector_x**2) + (missing_vector_y**2))
    print(colored("\n------------------------------------------------------------------------------------------", "green"))
    print(colored("Magnitude of the Missing Vector: " + "{:.4f}".format(missing_vector_magnitude), "green"), end="")
    print()

def missing_vector_direction(missing_vector_x, missing_vector_y):
    missing_vector_direction = np.rad2deg(np.arctan(abs(missing_vector_y / missing_vector_x)))
    print(colored("Direction of the Missing Vector: ", "green"), end="")
    if missing_vector_x > 0 and missing_vector_y == 0:
        print(colored("East", "green"))
    elif missing_vector_x > 0 and missing_vector_y > 0:
        print(colored(str("{:.4f}".format(missing_vector_direction)) + "° North of East", "green"))
    elif missing_vector_x == 0 and missing_vector_y > 0:
        print(colored("North", "green"))
    elif missing_vector_x < 0 and missing_vector_y > 0:
        print(colored(str("{:.4f}".format(missing_vector_direction)) + "° North of West", "green"))
    elif missing_vector_x < 0 and missing_vector_y == 0:
        print(colored("West", "green"))
    elif missing_vector_x < 0 and missing_vector_y < 0:
        print(colored(str("{:.4f}".format(missing_vector_direction)) + "° South of West", "green"))
    elif missing_vector_x == 0 and missing_vector_y < 0:
        print(colored("South", "green"))
    else:
        print(colored(str("{:.4f}".format(missing_vector_direction)) + "° South of East", "green"))
    print(colored("""
                                               __      __
                                              ( _\    /_ )
                                               \ _\  /_ / 
                                                \ _\/_ /_ _
                        Thank you for using     |_____/_/ /|
                           our program!         (  (_)__)J-)
                                                (  /`.,   /
                                                 \/  ;   /
                                                  | === |
------------------------------------------------------------------------------------------""", "green"))