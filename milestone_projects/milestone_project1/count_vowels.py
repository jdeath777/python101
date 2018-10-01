#Program to count the number of vowels in the string

#Take the input string from the user
my_input = input("Enter the string : ")

vowels = 0

#use for loop to count through the string and use if condition to 
#identify the vowels
for i in my_input:
    if(i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or       i == 'o' or i == 'O' or i == 'u' or i == 'U'):
        vowels = vowels + 1
print("The number of vowels in the string is: ", vowels)


