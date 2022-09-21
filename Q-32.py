''' Write a version of a palindrome recogniser that accepts a file name from the user,
reads each line, and prints the line to the screen if it is a palindrome.'''

import re 

def palindrome(string):
    string = re.sub(r'[^a-zA-Z]','',string).lower()
    
    reverse_string =''
    length = len(string)
    while length>0:
        length -= 1
        reverse_string += string[length]
    
    if reverse_string == string:
        return True
    else:
        return False

fobj = open("Q-32.txt", "r")
for x in fobj.readlines():
    print(x)
    print(palindrome(x))


'''def palindrome(string):
    string = string.lower()
    string = string.replace(' ', '')
    tem = ['.',',','!','?','\"',"\'","="]
    for i in tem:
        string = string.replace(i,"")

        tmp=''
        length = len(string)
        while length>0:
            length -= 1
            tmp += string[length]
    print(tmp)
    print(string)
    if tmp == string:
        return True
    else:
        return False

fobj = open("Q-32.txt", "r")
for x in fobj.readlines():
    print(x)
    print(palindrome(x))
'''