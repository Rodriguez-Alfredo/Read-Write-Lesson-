#!/bin/python3

#File to be opened needs to be in the same directory

months = open("month.txt") #opens the file and placed in a variable
print(months)
print(months.mode) #Shows the mode its in r/w/x
print(months.readable()) #True/Flase if its readable
print(months.read()) #shows the content in the file
months.seek(0) #be able to print items again
print(months.readline()) #shows one line 
months.seek(0)
print(months.readline())#shows second line
months.seek(0)
print(months.readlines()) #show items in new lines

months.seek(0)
for month in months: #Loop through the list items
	print(month.strip())	
	
months.close()


days = open("days.txt", "w") #Change file to write mode, to apened change "w" to "a"

days.write("Monday") #enter text in file
days.write("\nTuesday") #overwrite 

print(days)

days.close()

#Thank You TCM Security