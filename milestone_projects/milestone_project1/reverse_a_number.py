#Program to reverse a number

original = int(input("Enter a number: "))


num = original

rev = 0

while(num > 0):
    digit = num % 10
    rev = rev * 10 + digit
    num = num//10

print("The reverse of the number is: ", rev)
