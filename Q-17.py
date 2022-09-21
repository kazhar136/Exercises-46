'''
Write a version of a palindrome recognizer that
also accepts phrase palindromes such as "Go hang a
salami I'm a lasagna hog.", "Was it a rat I
saw?", "Step on no pets", "Sit on a potato pan,
Otis", "Lisa Bonet ate no basil",
"Satan, oscillate my metallic sonatas", "I roamed under
it as a tired nude Maori", "Rise to vote sir", or the
exclamation "Dammit, I'm mad!". Note that
punctuation, capitalization, and spacing are usually ignored
'''
import re
def palindrome(string):
    string = re.sub(r'[^a-zA-Z]','',string).lower()
    if string == string[::-1]:
        return True
    else:
        return False
    
print(palindrome("Go hang a salami? @= I'm a lasagna hog."))
print (palindrome("Was it a rat I saw?"))
print (palindrome("Dammit, I'm mad!"))


'''string ="Go hang a salami I'm a lasagna hog."
string = string.lower()

tem = ['.',',','!','?','\"',"\'"]
for i in tem:
    string = string.replace(i,"")
    tmp=''
    length = len(string)
    while length>0:
        length -= 1
        tmp += string[length]
print(string)'''