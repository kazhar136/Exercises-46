'''An anagram is a type of word play, the result of rearranging the letters of a word
or phrase to produce a new word or phrase, using all the original letters exactly
once; e.g., orchestra = carthorse, A decimal point = I'm a dot in place. Write a
Python program that, when started 1) randomly picks a word w from given list of words,
2) randomly permutes w (thus creating an anagram of w), 3) presents the anagram to
the user, and 4) enters an interactive loop in which the user is invited to guess the
original word. It may be a good idea to work with (say) colour words only.
The interaction with the program may look like so:
>>> import anagram
Colour word anagram: onwbr
Guess the colour word!
black
Guess the colour word!
brown
Correct!
'''
import random
def letter(word):
    word=list(word)
    random.shuffle(word)
    return ''.join(word)
def main():
    random_color = random.choice(['red','orange','yellow','green','blue','purple','white','black'])
    object_function = letter(random_color)
    print("Color word anagram:",object_function)
    while True:
        guess=input("Guess the color word\n")
        if guess == random_color:
            print("Correct!")
            break
if __name__=="__main__":
    main()
