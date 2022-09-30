'''
An anagram is a type of word play, the result of rearranging the letters of
a word or phrase to produce a new word or phrase, using all the original
letters exactly once; e.g., orchestra = carthorse. Using the word list at
http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that
finds the sets of words that share the same characters that contain the most
words in them.
'''


def anagram(str1,str2):
    if len(str1)==0 and len(str2)==0:
        return False

    str1 = str1.lower()
    str2 = str2.lower()

    str1.replace(" ","")
    str2.replace(" ","")

    str1_list = list(str1)
    str1_list.sort()

    str2_list = list(str2)
    str2_list.sort()

    if str1_list == str2_list:
        return  True
    else:
        return False
str1 = input("Enter First string: ")
str2 = input("Enter Second string: ")

if anagram(str1,str2):
    print("Anagram")
else:
    print("not Anagram")
