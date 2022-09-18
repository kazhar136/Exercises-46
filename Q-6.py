'''Define a function sum() and a function multiply() that sums and
multiplies (respectively) all the numbers in a list of numbers.
For example, sum([1, 2, 3, 4]) should return 10, and 
multiply([1, 2, 3, 4]) should return 24.'''

def add(list):
    sum=0
    for i in list:
        sum=sum+i
    return sum

def multi(list1):
    mul=1
    for i in list1:
        mul=mul*i
    return mul

ob=add([1,2,3,4])
ob1=multi([1,2,3,4])
print("sum is :",ob)
print("multiplie is :",ob1)