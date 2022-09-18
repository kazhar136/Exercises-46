''' A pangram is a sentence that contains all the letters of the English alphabet
at least once, for example: The quick brown fox jumps over the lazy dog.
Your task here is to write a function to check a sentence to see if it is a
pangram or not. '''

def pangram(str):
    a = "abcdefghijklmnopqurstuvwxyz"
    for x in a:
        if x not in str.lower():
            return False
    return True

str = "The quick brown fox jumps over the lazy dog  "
obj = pangram(str)

if obj == True:
    print("Sentence is pangram")
else:
    print("not pangram")

 