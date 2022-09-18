''' Write a function find_longest_word() that takes a list of words and returns the
length of the longest one. '''

def longest_word(n):
    largest = len(n[0])
    for x in n:
        if len(x)>largest:
            largest = len(x)
    return largest

words = input("Enter the Words: ")
n = words.split()
print(longest_word(n))