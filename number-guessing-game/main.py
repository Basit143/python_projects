import random

min_number = 1
max_number = 100

secret_number = random.randint(min_number, max_number)

attempts = 0
guess = None

while guess != secret_number:
    attempts += 1
    guess = int(input(f"Guess a number between {min_number} and {max_number}: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts!")