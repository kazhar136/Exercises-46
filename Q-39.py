''' Write a program able to play the "Guess the number"-game, where the number to be
guessed is randomly chosen between 1 and 20. (Source: http://inventwithpython.com)
This is how it should work when run in a terminal '''

import random

my_num = random.randint(1,20)
name = input("Hello what is Your Name :")

print("Well,",name,',',"I am thinking of a number between 1 to 20. Can you gaess it \n")
while True:
    user_num = int(input("enter your guess: "))
    if( my_num==user_num ):
        print("Congratulation!!!!.... yes your right")
        break
    elif (my_num>user_num):
        print("My Number is greater than the number you entered. try again:",end='\n\n' )
    else:
        print("My Number is smaller than the number you entered. try again:",end='\n\n')