#!/bin/python3

# number guess implements a function which simulates a pair of dice being rolled, the user has to guess the sum

from random import randint
from time import sleep

def get_user_guess():
    guess = int(input("Guess the sum of the dice: "))
    return guess

def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_roll = number_of_sides*2
    print("The maximum roll sum is %d" %(max_roll))
    guess = get_user_guess()
    if(guess > max_roll):
        print("This is too high! Your guess must be less than %d" %(max_roll))
    else:
        print("rolling dice...")
        sleep(2)
        print("First roll is %d" %(first_roll))
        sleep(1)
        print("Second roll is %d" %(second_roll))
        sleep(1)
        total_roll = first_roll + second_roll
        if(total_roll != guess):
            print("Sorry! You were wrong!")
        else:
            print("Congratulations, you guessed correctly!!")

roll_dice(6)


