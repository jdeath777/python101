#Check the palindrome of a string

str = input("Enter the string: ")

str_len = len(str)

rev = str[-1:-(str_len + 1):-1]

if(rev == str):
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")
