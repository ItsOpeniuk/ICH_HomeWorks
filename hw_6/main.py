from random import randint


num = randint(1, 20)
guess = int(input("Enter your guess: "))
attempts = 10
while True:
    if guess < num:
        print("Too low try again!")
        attempts -= 1
        guess = int(input(f"Enter your guess, You have {attempts} attempts left"))
        attempts -= 1
    elif guess > num:
        print("Too high try again!")
        attempts -= 1
        guess = int(input(f"Enter your guess, You have {attempts} attempts left"))
    elif guess == num:
        print("Congratulations!")
        break
