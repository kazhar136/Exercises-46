''' Write a function find_longest_word() that takes a list of words and returns the
length of the longest one. Use only higher order functions. '''

import functools

def find_longest_word(lst):
    new_list = list(map(len,lst))
    return functools.reduce(lambda x,y : x if x>y else y, new_list)

lst1 = []
i = 0
n = int(input("How many number you want to list: "))
while i<n:
    a = input("Enter the Word: ")
    lst1.append(a)
    i+=1

print("lingest word is",find_longest_word(lst1))