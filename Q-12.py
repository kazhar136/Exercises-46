''' Define a procedure histogram() that takes a list of integers and 
prints a histogram to the screen. For example, histogram([4, 9, 7]) 
should print the following:
****
*********
******* '''

def histogram(list):
    for x in list:
        print(x * '*')

list1 = []
list2 = int(input("How many Number You Want To list:"))
for i in range(list2):
    data = int(input("Enter the list :"))
    list1.append(data)
histogram(list1)
