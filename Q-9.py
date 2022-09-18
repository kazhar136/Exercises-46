'''
Write a function is_member()that takes a value
(i.e. a number, string, etc) x and a list of
values a, and returns True if x is a member of a,
False otherwise.(Note that this is exactly what
the in operator does, but for the sake of the
exercise you should pretend Python did not
have this operator.)
'''

def is_member(item,list_var):
    list_length = len(list_var)
    for i in range(list_length):
        if item==list_var[i]:
            return True
    return False

abc = [1,4,6,9,34]
print(is_member(9,abc))
print(is_member(11,abc))
    
