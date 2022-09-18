''' The function max() from exercise 1) and the function max_of_three() from exercise 2)
will only work for two and three numbers, respectively. But suppose we have a much larger
number of numbers, or suppose we cannot tell in advance how many they are? Write a
function max_in_list() that takes a list of numbers and returns the largest one. '''

def max_in_list(list):
    maximum = 0
    for x in list:
        if x > maximum:
            maximum = x
    return maximum

list1 = []
list2 = int(input("How many Number You want list:"))
i = 0
while i<list2:
    data = int(input("Enter The add number in list"))
    i=i+1
    list1.append(data)

ob = max_in_list(list1)
print("Maximum Number in list is",ob)