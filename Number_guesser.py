from random import randint
from sys import exit
while True:
    try:
        top_of_range = int(input("Type a number: "))
        break
    except ValueError:
        print("Please, type a number.")
        continue
if top_of_range <= 0:
    print("Type a number greater than 0 next time.")
    exit()

random_number = randint(0, top_of_range)
guesses = 0
while True:
    guesses += 1
    try:
        user_guess = int(input("Make a guess: "))
    except ValueError:
        print("Please, type a number.")
        continue
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You need to go lower")
    else:
        print("You need to go higher")
print(f'"You got it in {guesses} guess/es"')
print("Thanks for playing!")