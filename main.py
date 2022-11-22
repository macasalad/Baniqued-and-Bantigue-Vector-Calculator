import numpy as np
from termcolor import colored

from greetings import greetings
from missing_resultant import resultant_magnitude
from missing_resultant import resultant_direction
from missing_vector import missing_vector_magnitude
from missing_vector import missing_vector_direction

resultant_vector_x, resultant_vector_y, sum_vectors_x, sum_vectors_y, missing_vector_x, missing_vector_y = [0, 0, 0, 0, 0, 0]
resultant_vector_count = 0
ans = "yes"

greetings()

print("""What are you solving for?
[A] Resultant Vector
[B] Missing Vector""")

missing_vector_type = input("Enter your answer: ")
print()

if missing_vector_type.lower() == "a":
    while ans.lower() == "yes":
        ans = input("Would you like to add a vector (Yes/No): ")
        if ans.lower() == "yes":
            vector_magnitude = float(input("Enter Magnitude of Vector: "))
            vector_direction = float(input("Enter Direction of Vector (in degrees, measured from the positive x-axis): "))
            print()
            resultant_vector_x += (vector_magnitude * (np.cos(np.deg2rad(vector_direction))))
            resultant_vector_y += (vector_magnitude * (np.sin(np.deg2rad(vector_direction))))
        elif ans.lower() == "no":
            if resultant_vector_x == 0 and resultant_vector_y == 0:
                print(colored("Input some information first!\n", "red"))
                ans = "yes"
            else:
                resultant_magnitude(resultant_vector_x, resultant_vector_y)
                resultant_direction(resultant_vector_x, resultant_vector_y)
        else:
            print(colored("Input is invalid.\n", "red"))
            ans = "Yes"

elif missing_vector_type.lower() == "b": 
    while ans.lower() == "yes":
        ans = input("Would you like to add a vector (Yes/No): ")
        if ans.lower() == "yes":
            vector_magnitude = float(input("Enter Magnitude of Vector: "))
            vector_direction = float(input("Enter Direction of Vector (in degrees, measured from the positive x-axis): "))
            resultant_or_not = input("Is this the Resultant Vector (Yes/No): ")
            if resultant_or_not.lower() == "yes":
                print()
                resultant_vector_x += (vector_magnitude * (np.cos(np.deg2rad(vector_direction))))
                resultant_vector_y += (vector_magnitude * (np.sin(np.deg2rad(vector_direction))))
            elif resultant_or_not.lower() == "no":
                print()
                sum_vectors_x += (vector_magnitude * (np.cos(np.deg2rad(vector_direction))))
                sum_vectors_y += (vector_magnitude * (np.sin(np.deg2rad(vector_direction))))
                resultant_vector_count += 1
            else:
                print(colored("Input is invalid.\n", "red"))
            missing_vector_x = resultant_vector_x - sum_vectors_x
            missing_vector_y = resultant_vector_y - sum_vectors_y
        elif ans.lower() == "no":
            if resultant_vector_x == 0 and resultant_vector_y == 0 and sum_vectors_x == 0 and sum_vectors_x == 0:
                print(colored("Input some information first!\n", "red"))
                ans = "yes"
            else:
                if resultant_vector_count == 1:
                    missing_vector_magnitude(missing_vector_x, missing_vector_y)
                    missing_vector_direction(missing_vector_x, missing_vector_y)
                else:
                    print(colored("There should only be ONE resultant vector. Please try again.\n", "red"))
        else:
            print(colored("Input is invalid.\n", "red"))
            ans = "yes"

else:
    print(colored("Input is invalid. Please enter either 'A' or 'B'.", "red"))