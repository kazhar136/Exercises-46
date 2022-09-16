''' Write a program that maps a list of words into a list of integers representing
the lengths of the correponding words '''

Words = ['Azhar','Abhianv','Vikram','Anuj','Deepak','vikas']
 
Integers = []
 
for i in range(len(Words)):
    Integers.append(len(Words[i]))
 
print ("List of words:",Words)    
print ("List of words length:",Integers)