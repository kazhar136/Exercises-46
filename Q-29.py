"""
Using the higher order function filter(), define a function filter_long_words() that takes a list of words and an
integer n and returns the list of words that are longer than n.
"""


def long_words(words, n):
    return list(filter(lambda x : len(x) > n, words))


print(long_words(['test', 'not'], 2))
