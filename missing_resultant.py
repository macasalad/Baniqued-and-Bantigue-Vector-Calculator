import numpy as np
from termcolor import colored

def resultant_magnitude(resultant_vector_x, resultant_vector_y):
    resultant_vector_magnitude = np.sqrt((resultant_vector_x**2) + (resultant_vector_y**2))
    print(colored("\n------------------------------------------------------------------------------------------", "green"))
    print(colored("Magnitude of the Resultant Vector: " + "{:.4f}".format(resultant_vector_magnitude), "green"))

def resultant_direction(resultant_vector_x, resultant_vector_y):
    resultant_vector_direction = np.rad2deg(np.arctan(abs(resultant_vector_y / resultant_vector_x)))
    print(colored("Direction of the Resultant Vector: ", "green"), end="")
    if resultant_vector_x > 0 and resultant_vector_y == 0:
        print(colored("East", "green"))
    elif resultant_vector_x > 0 and resultant_vector_y > 0:
        print(colored(str("{:.4f}".format(resultant_vector_direction)) + "° North of East", "green"))
    elif resultant_vector_x == 0 and resultant_vector_y > 0:
        print(colored("North", "green"))
    elif resultant_vector_x < 0 and resultant_vector_y > 0:
        print(colored(str("{:.4f}".format(resultant_vector_direction)) + "° North of West", "green"))
    elif resultant_vector_x < 0 and resultant_vector_y == 0:
        print(colored("West", "green"))
    elif resultant_vector_x < 0 and resultant_vector_y < 0:
        print(colored(str("{:.4f}".format(resultant_vector_direction)) + "° South of West", "green"))
    elif resultant_vector_x == 0 and resultant_vector_y < 0:
        print(colored("South", "green"))
    else:
        print(colored(str("{:.4f}".format(resultant_vector_direction)) + "° South of East", "green"))
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