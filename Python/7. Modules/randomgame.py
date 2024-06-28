#generate a number 1-10
import sys #so you can play this game on terminal

from random import randint
answer = randint(int(sys.argv[1]), int(sys.argv[2]))#these classify the inputs you do on terminal
#get an input from user
#check that input is a number 1-10
while True:
    try:
        guess = int(input('Guess a number 1~10: '))

        if 0 < guess < 11:
            if guess == answer:
                print('You are a genius!!!!!')
                break
            else:
                print('Try again buddy')
                continue
        else:
            print('hey bozo I said 1-10')
    except ValueError:
        print('Please enter a number')
        continue
#check if number is right guess.

#otherwise, ask again.