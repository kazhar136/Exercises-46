#Exercise 16
 
#Write a function filter_long_words() that takes a list of words and
#an integer n and returns the list of words that are longer than n.
 
def filter_long_words(list1,num1):
    new_list = []
    for i in list1:
        if len(i)>num1:
            new_list.append(i)
    return new_list

list1 = []
n = int(input("How many number you want to list: "))
i = 0
while i<n:
    a = input("Enter the word: ")
    list1.append(a)
    i+=1

num1 = int(input("Enter any Number: "))
print(filter_long_words(list1,num1))