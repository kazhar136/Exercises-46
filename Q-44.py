''' Your task in this exercise is as follows:
Generate a string with N opening brackets ("[") and N closing brackets ("]"), in
some arbitrary order. Determine whether the generated string is balanced; that is,
whether it consists entirely of pairs of opening/closing brackets (in that order),
none of which mis-nest.
Examples:
   []        OK   ][        NOT OK
   [][]      OK   ][][      NOT OK
   [[][]]    OK   []][[]    NOT OK

'''
from math import remainder


var1  = "[]"
var2 = "[[]]"
var3 = "[[[]]]"
var4 = "]["
var5 = "][]["
var6 = "[]][[]"

def string(var):
    length = len(var)
    if length % 2 == 0:
        half = int(length / 2)
        first_var = '[' * half 
        last_var = ']' * half 
        if var[0:half] == first_var and var[half:length] == last_var:
            return 'OK'
        else:
            return 'NOT OK'
    else:
        return 'NOT OK'

print(string(var1))
print(string(var2))
print(string(var3))
print(string(var4))
print(string(var5))
print(string(var6))
