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


#fast-fats, break-baker,arm-ram