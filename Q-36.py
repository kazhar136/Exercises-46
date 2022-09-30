
'''
A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in
either the written record of a language, the works of an author, or in a single text.
Define a function that given the file name of a text will return all its hapaxes.
Make sure your program ignores capitalization.
'''
from fileinput import filename
import re 

def hapax(file):
  filename = open(file)
  word_list =re.findall('\w+',filename.read().lower())
  word_dict = {key : 0 for key in word_list } 
  #print(word_dict)
  for word in word_list:
    word_dict[word] +=1
  for word1 in word_dict:
    if word_dict[word1] == 1:
      print(word1 , end=" ")



hapax("Q-36.txt")
  










'''import re
def hapax_checker(file_name):
    f = open(file_name, 'r').read()
    #substitutue all non letters with spaces
    f = re.sub(r'[^A-Za-z]', ' ', f)
    words = f.lower().split(' ')
    print(words)

    for line in f:
        words.append(line.lower().split())
    #filter swords which occurs once
    hapaxes = list(filter(lambda x: words.count(x) == 1, words))
    return hapaxes

file_name = input('Please enter your file name')
print(hapax_checker(file_name))

'''

'''

def char_freq_table(file_name):

  file = open(file_name, 'r')

  str = filter(lambda x: x not in [' ','\n'], file.read())
  freq = {}
  for c in str:
    if c in freq:
      freq[c] += 1
    else:
      freq[c] = 1
   
   for char in sorted(freq.items(), key=lambda x: x[1], reverse=True):
	print(char[0], freq[char[0]])
    
    

#test
file_name = "ex. poem.txt"
char_freq_table(file_name)'''














"""A hapax legomenon (often abbreviated to hapax) is a word which occurs 
only once in either the written record of a language, the works of an 
author, or in a single text. Define a function that given the file name 
of a text will return all its hapaxes. Make sure your program ignores 
capitalization.

def hapax(file_name):
	words = [] # Prepare our words list
	# Fill the words list
	with open(file_name, 'r') as f:
		for line in f:
			words += line.lower().split()

	# Filter the hapaxes from the rest
	hapaxes = list(filter(lambda x: words.count(x) == 1, words))
	
	# Return what we need
	return hapaxes

#test
print(hapax('hapax.txt'))
"""

