''' In English, the present participle is formed by adding the suffix -ing to the infinite
form: go -> going. A simple set of heuristic rules can be given as follows:
If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee,
etc.)
If the verb ends in ie, change ie to y and add ing
For words consisting of consonant-vowel-consonant, double the final letter before
adding ing By default just add ing
Your task in this exercise is to define a function make_ing_form() which given a verb
in infinitive form returns its present participle form. Test your function with words
such as lie, see, move and hug. However, you must not expect such simple rules to work
for all cases. '''

def present_part(a):
    b = a[:-1]
    if a.endswith("ee") or a=="be":
        a = a + "ing"
        return a
    elif a.endswith("ie"):
        a = a[:-2]
        a = a + "ying"
        return a
    elif a.endswith('e'):
        a = a[:-1]
        a = a + "ing"
        return a
    elif b.endswith('a') or b.endswith('e') or b.endswith('i') or b.endswith('o') or b.endswith('u'):
        a = a + a[-1] + "ing"
        return a
    else:
        a = a + "ing"
        return a


b = input("Give me a word : ")
c = present_part(b)
print(c)