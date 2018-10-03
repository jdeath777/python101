#Program to reverse a string

#take the input of the string
str = input("Enter the string: ")

#Get the length of the string
str_len = len(str)

#Reverse the string from right to left using -1
#The -1 at the end is used to tell the slicing to be done from
#right to left
rev = str[-1:-(str_len + 1):-1]

print("The reverse of the string is: ",rev)
