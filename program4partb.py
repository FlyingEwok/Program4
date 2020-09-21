'''Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, 	return instead of the empty string.''' 

#Print out program purpose
print("This program will ask you to enter a string and then will print out the first 2 characters and the last 2 characters")

#Ask user to enter a string
string = input("Enter whatever you want for this string: ")

#Create a function that will return nothing if the string is less than 2 or return the first 2 and last 2 chars from the string
def stringBothEnds(str):
	if len(str) < 2:
		return ''
	return string[0:2] + string[-2:]

#Print the string using the created function
print(stringBothEnds(string)) 
