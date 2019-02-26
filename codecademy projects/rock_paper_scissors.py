#!/bin/python3

# this simulates a game of rock paper scissors between the computer and the user

from random import randint

options = ["rock", "paper", "scissors"]
message = {
    "tie": "Yawn, it's a tie!",
    "won": "Yay you won!",
    "lost": "Aww you lost!"
}

def decide_winner(user_choice, computer_choice):
    print("You: " + user_choice)
    print("Computer: " + computer_choice)
    if(user_choice == computer_choice):
        print(messages["tie"])
    #scenarios where the user wins
    elif((user_choice="rock" & computer_choice="scissors") | (user_choice="paper" & computer_choice="rock") | (user_choice="scissors" & computer_choice="paper")):
        print(messages["won"])
    #scenarios where the user loses
    else:
        print(messages["lost"])

def play_rps():
    user_choice = input("Please enter one of: rock, paper or scissors: ")
    computer_choice = options[randint(0,2)]
    decide_winner(user_choice, computer_choice)

play_rps()