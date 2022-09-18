'''Define a function that computes the length of a given list or string.
(It is true that Python has the len() function built in, 
but writing it yourself is nevertheless a good exercise.)'''

def length(word):
    count = 0
    for x in word:
        count=count+1
    return count

word= input("Enter the String :")
print("The length of String is ",length(word))