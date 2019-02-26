#!/bin/python3

# this tip calculator assumes a meal cost of $44.50, a restaurant tax of $6.75 and a 15% tip.

meal = 44.5
tax = 6.75/100
tip = 15/100

meal = meal + meal*tax

total = meal + meal*tip

print(total)