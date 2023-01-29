import random

random_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty: type 'easy' or 'hard': ")

attempts = 0
if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess : "))
    if guess == random_number:
        print(f"You got it! The answer was {random_number}.")
        break
    else:
        attempts -= 1
        if guess < random_number:
            print("Too low.")
        else:
            print("Too high.")
        print("Guess again.")

if attempts == 0:
    print(f"You've run out of guesses, you lose. The correct number was {random_number}")
