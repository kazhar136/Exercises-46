'''
Represent a small bilingual lexicon as a Python dictionary
in the following fashion:

{"merry":"god", "christmas":"jul", "and":"och", "happy":gott",
"new":"nytt", "year":"år"}

and use it to translate your Christmas cards from
English into Swedish. Use the higher order function map()
to write a function translate()that takes a list of English
words and returns a list of Swedish words.
'''
def translate(list1):
    dic = {"merry":"god", "christmas":"jul", "and":"och",\
           "happy":"gott","new":"nytt", "year":"år"}
    return list(map(lambda x:dic[x] if x in dic else False, list1))
    
ab = ['merry','and','new','sad']  
print(translate(ab))