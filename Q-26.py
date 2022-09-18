"""Using the higher order function reduce(), write a function max_in_list() 
that takes a list of numbers and returns the largest one. Then ask yourself:
why define and call a new function, when I can just as well call the reduce() 
function directly?"""

import functools

def max_in_list(list):
    return functools.reduce(lambda x,y : x if x>y else y, list)

list = [4,5,3,21,5]
print(max_in_list(list))

