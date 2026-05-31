import random

print("Number Guessing Game")
print("Range lies from 1 to 100")

number = random.randint(1, 100)

attempts = 0
max_attempts = 5

while attempts < max_attempts:

    guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}. Your guess: "))
    attempts += 1

    if guess < 1 or guess > 100:
        print("Number does not lie in the range. Please try again.")
        continue

    if guess == number:
        print("Congrats! Your answer is correct.")
        break

    elif guess < number:
        print("Value is small.")

    else:
        print("Value is large.")

if attempts == max_attempts and guess != number:
    print(f"Game Over! The number was {number}.")
