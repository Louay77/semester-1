import random

# Get user to input how many random numbers they want
try:
    user_input: (int(input("how many random number?")))
except:
    print("integer expected")
else:

# Generate this many random numbers
    1st_numbers = random.randint(range(user_input))

# Write the random numbers to a file named random.txt, one number per line
    with open("random.txt") as infile:
        