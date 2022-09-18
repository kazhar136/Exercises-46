'''Define a function is_palindrome() that recognizes palindromes 
(i.e. words that look the same written backwards).
For example, is_palindrome("radar") should return True.'''

def is_palindrome(word):
    b=word[-1::-1]
    if word==b:
        return True
    else:
        return False
a = input("Enter String :")    
ob =  is_palindrome(a)
print(ob)