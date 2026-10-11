import random

random_number = random.randint(0, 100)

while True:
    guess = int(input("Guess the number: "))
    if guess < random_number:
        print("Nope try higher")
    elif guess > random_number:
        print("Nope try lower")
    else:
        print("Thats right!")
        print("You won!")
        break