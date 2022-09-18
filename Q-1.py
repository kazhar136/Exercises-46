'''Define a function max() that takes two numbers as arguments and returns the largest 
of them.Use the if-then-else construct available in Python. (It is true that Python has 
the max()function built in, but writing it yourself is nevertheless a good exercise.)'''


def maximum(num1,num2):
    if num1>num2:
        return num1
    elif num1<num2:
        return num2
    else:
        return None

if __name__ == '__main__':
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    ob=maximum(a,b)
    print("Maximum Number is :", ob)
