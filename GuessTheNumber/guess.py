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


def computer_guess(x): #computer guesses your number with low or high clues
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high because low = high

        feedback = input(f'Is {guess} too high (H), too low (L), or correct (O) ??')
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1
    print(f"Computer guessed your number, {guess}, correctly!")

computer_guess(100)