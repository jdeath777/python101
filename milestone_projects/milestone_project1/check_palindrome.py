#Check if the string is a palindrome or not

str =int(input("Enter the string:"))

temp = str

rev = 0

dig = 0

while(str>0):
    dig = str%10
    rev = rev * 10 + dig
    str = str//10

if(temp == rev):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
