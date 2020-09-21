'''Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with '	ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.'''

#Print out program purpose
print("This program will ask you to enter a string and then will print out the string with ing or ly or just return the string")

#Ask user to enter a string
string = input("Enter whatever you want for this string: ")

#Create a function that will return ing if the string is greater than 3 or return ly if the string already ends in ing and return the string if characters in string is less than 3
def stringFunc(str):
	ingEnd = string.endswith('ing')
	if len(str) >= 3 and not ingEnd:
		return string + 'ing'
	elif ingEnd:
		return string + 'ly'
	else:
		return string
		
#Print the string using the created function
print(stringFunc(string)) 

print("Hello")