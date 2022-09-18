''' Define a function overlapping() that takes two lists and returns True if they have
at least one member in common, False otherwise. You may use your is_member()
function, or the in operator, but for the sake of the exercise, you should (also)
write it using two nested for-loops. '''

def overlapping(lst1,lst2):
    for x in lst1:
        for i in lst2:
            if x==i:
                return True
    return False

l1 = [1,3,6,4,8]
l2 = [2,5,7,4,5]

ob = overlapping(l1,l2)
print(ob)