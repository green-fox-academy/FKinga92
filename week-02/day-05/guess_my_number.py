# Exercise
# Write a program where the program chooses a number between 1 and 100. The player is then asked to enter a guess. 
# If the player guesses wrong, then the program gives feedback and ask to enter an other guess until
# the guess is correct.
# Make the range customizable (ask for it before starting the guessing).
# You can add lives. (optional)
# Example
# I've the number between 1-100. You have 5 lives.
# 20
# Too high. You have 4 lives left.
# 10
# Too low. You have 3 lives left.
# 15
# Congratulations. You won!

import random

custom_range = input("Please choose a range by entering two numbers: ")
range_start, range_end = custom_range.split()
my_number = random.randint(int(range_start), int(range_end))
lives = 5
your_number = int(input("I've chosen a number between " +  range_start + "-" + range_end + ". You have 5 lives. Guess my number: "))
while lives > 0:
    if your_number == my_number:
        print("Congratulations. You won!")
        lives = 0
    elif your_number > my_number:
        lives -= 1
        if lives > 0:
            print("Too high. You have " + str(lives) + " lives left.")
            your_number = int(input("Guess again: "))
        else:
            print("No more lives left. Game over.")
            lives = 0
    else:
        lives -= 1
        if lives > 0:
            print("Too low. You have " + str(lives) + " lives left.")
            your_number = int(input("Guess again: "))
        else:
            print("No more lives left. Game over.")
            lives = 0