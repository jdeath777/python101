#To sort a sentence using string split()

str = input("Enter the string to sort: ").split(' ')



str.sort()

for  i in str:
    print(i,end='')


