''' Write a program that given a text file will create a new text file in which all
the lines from the original file are numbered from 1 to n (where n is the number of
lines in the file). '''

old_file = open("Q-33.txt","r")
new_file = open("Q-37_newfile_numbered.txt","w")
lines = old_file.readlines()

count = 0
for line in lines:
    count+=1
    output_line = str(count)+". "+line
    new_file.write(output_line)

print("Lines are numbered")
old_file.close()
new_file.close()