''' Write a program that maps a list of words into a list of integers representing
the lengths of the correponding words. Write it in three different ways: 1) using a
for-loop, 2) using the higher order function map(), and 3) using 
list comprehensions. '''

def map1(lst):
    lst2 = []
    for x in lst:
        lst2.append(len(x))
    return lst2

def map2(lst):
   return list(map(len,lst))

def map3(lst):
    return [len(i) for i in lst]

lst1 = []
i = 0
n = int(input("How many number you want to list: "))
while i<n:
    a = input("Enter the Word: ")
    lst1.append(a)
    i+=1
print(map1(lst1))
print(map2(lst1))
print(map3(lst1))