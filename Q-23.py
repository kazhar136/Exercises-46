''' Define a simple "spelling correction" function correct() that takes a string and
sees to it that 1) two or more occurrences of the space character is compressed into
one, and 2) inserts an extra space after a period if the period is directly followed
by a letter. E.g. correct("This   is  very funny  and    cool.Indeed!") should return
"This is very funny and cool. Indeed!" Tip: Use regular expressions! '''


def Correct(string):
    spaces = 0
    correction = ""
    for c in string:
        if c==" ":
            spaces+=1
            if spaces>1:
                pass
            elif spaces==1:
                correction+=c
        elif c==",":
            correction=correction+c+" "
        else:
            correction+=c
            spaces=0
    return correction
a = "This   is  very funny  and    cool.Indeed!"
print(Correct(a))