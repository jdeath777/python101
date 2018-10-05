#Program to remove the punctuation mark

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

str = input("Enter the string to: ")

#declare a empty string to store the replaced string
result = ""

for i in str:
    if(i not in punctuations):
        result += i
print(result)
