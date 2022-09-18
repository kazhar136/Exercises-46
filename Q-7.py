'''Define a function reverse() that computes the reversal of a string. For example, 
reverse(“I am testing”) should return the string “gnitset ma I”.'''

def reverse(text):
    new = ""
    n = len(text)
    while n>0:
        n-=1
        new += text[n]
    return new

ob=reverse("I am testing")
print(ob)

#or

"""
def reverse(rev):
    for x in range(len(rev)-1,-1,-1):
        print(rev[x],end="")

reverse("I am testing")
"""    

