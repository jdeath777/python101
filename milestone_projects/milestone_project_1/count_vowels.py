#Program to count the number of vowels in a string

print("Enter your input: ")
my_input = input()

vowels = 0

for item in my_input:
        if(item == "a" or item == "A" or item == "e" or item =="E" or item == "i" or item == "I" or item == "o" or item == "O" or item == "u" or item == "U"):

            vowels = vowels + 1
            print("The number of vowels are:", vowels)
