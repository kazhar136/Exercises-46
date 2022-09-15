'''Define a function reverse() that computes the reversal of a string. For example, 
reverse(“I am testing”) should return the string “gnitset ma I”.'''

def reverse(rev):
    d=rev[::-1]
    return d

ob=reverse("I am testing")
print(ob)