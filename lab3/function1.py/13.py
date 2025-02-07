import random

def guess_the_number():
    name = input("Hello! What is your name? ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    number_to_guess = random.randint(1, 20)
    guess = None
    guesses_taken = 0
    
    while guess != number_to_guess:
        guess = int(input("Take a guess: "))
        guesses_taken += 1
        
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
    
    print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")

guess_the_number()
