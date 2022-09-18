''' Write a function translate() that will translate a text into 
"rövarspråket" (Swedish for "robber's language"). That is, 
double every consonant and place an occurrence of "o" in between. 
For example, translate("this is fun") should return the string "tothohisos
 isos fofunon" '''



def translate(s):
    string = ""
    for x in s:
        string = string + x
        if x not in ["a","e","i","o","u",""," "]:
            string = string+ "o"+x
    return string

ob= translate("THiS is   fun")
print(ob)
