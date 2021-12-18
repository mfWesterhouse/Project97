import random
print("Number Guessing Game")
number = random.randint(1,9)
chances = 0 
print("Guess a number between one and nine")

while chances < 5:
    guess = int(input("Enter your guess : "))
    if guess == number:
        print("You won!")
        break
    elif guess < number:
        print("Your guess is too low", guess)

    else :
        print("Your guess was too high", guess)
    chances += 1
if not chances < 5:
    print("You lost! The number is ", number)
