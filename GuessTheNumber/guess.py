import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0 #random number starts at 1 so guess never be random number
    while guess!= random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        #We have to use int before input because without int we get a error for compare string and int
        print(guess)
        
        if (guess < random_number):
            print("Sorry, guess again. Too low.")
        elif (guess > random_number):
            print("Sorry, guess again. Too high")
        
    print(f"Congrats! You have guessed the number {random_number} correctly!")

guess(10)
