'''Write a function that takes a character (i.e. a string of length 1) 
and returns True if it is a vowel, False otherwise.'''

'''def vowel(x):
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='A' or x=='E' or x=='I' or x=='O' or x=='U':
        return True
    else:
        return False'''

def vowel(x):
    list = ["a","e","i","o","u"]
    for i in list:
        if i == x:
            return True
        else:
            return False

word = input("Enter The Word :")
string = word.lower()
ob = vowel(string)
print(ob)
