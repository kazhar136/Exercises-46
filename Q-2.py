'''Define a function max_of_three() that takes three numbers as arguments 
and returns the largest of them.'''

def max(a,b,c):
    if (a>b) and (a>c):
        return a
    elif (b>a) and (b>c):
        return b
    elif (c>a) and (c>b):
        return c
    else:
        return None

ob = max(7,9,8)
print("Largest Number is :",ob)