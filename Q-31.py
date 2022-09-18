'''
Implement the higher order functions map(), filter()and reduce().
(They are built-in but writing them yourself
may be a good exercise.
'''

def myreduce(lst):
    v = 0
    for v in lst:
        s = v+1
        if lst[v]> lst[s]:
            return lst[v]
        else:
            return lst[s]



def mymap(func,seq):
    ini = []
    for item in seq:
        ini.append(func(item))
    return ini

def myfilter(func,seq):
    ini = []
    for item in seq:
        if func(item)==True:
            ini.append(item)
    return ini




print(mymap(len,['abc','abcd']))
print(myfilter(lambda x:x>5,[1,3,5,7,9]))
print(myreduce([2,5,8,6,4]))