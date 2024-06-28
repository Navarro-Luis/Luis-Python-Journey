
import random


def run_guess(guess,answer):
    if 0 < guess < 11:
        if guess == answer:
            print('You are a genius!!!!!')
            return True
    else:
        print('hey bozo I said 1-10')
        return False


if __name__ == '__main__': # makes it so this only runs if main file, otherwise test file runs the game when we test which we dont want.
    answer = random.randint(1,10)    
    while True:
        try:
            guess = int(input('Guess a number 1~10: '))
            if (run_guess(guess,answer)):
                break
        except ValueError:
            print('Please enter a number')
            continue
