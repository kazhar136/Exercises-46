''' Write a program that will calculate the average word length of a text stored in a
file (i.e the sum of all the lengths of the word tokens in the text, divided by the
number of word tokens). '''

from functools import reduce

fobj = open("Q-38.txt","r")
file = fobj.read().split()
new_list = list(map(len,file))
sum = reduce(lambda x,y: x+y, new_list)
avrg = sum/len(new_list)

print("average word length of a text: ",avrg)
