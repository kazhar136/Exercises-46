''' Define a function generate_n_chars() that takes an integer n and 
a character c and returns a string, n characters long, consisting 
only of c:s. For example, generate_n_chars(5,"x") should return the 
string "xxxxx". (Python is unusual in that you can actually write an 
expression 5 * "x" that will evaluate to "xxxxx". For the sake of the 
exercise you should ignore that the problem can be solved in this 
manner.) '''

def generate(i,c):
    answer = ""
    for x in range(i):
        answer = answer+c
    print(answer)

i = int(input("Enter any Number: "))
c = input("Enter string: ")

generate(i,c)