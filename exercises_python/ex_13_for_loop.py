#using for loop to do things

count = [1,2,3,4,5]

fruits = ['apples', 'mangoes', 'oranges', 'pears']

change = [1, 'paise', 2, 'rupees', 3, 'lakhs']


# first kind of for-loop goes through a list
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

#list of mixed lists
for i in change:
    print(f"I got {i}")

#empty list

elements = []

#using range function to do 0 to 5 counts

for i in range(0,6):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Elements was: {i}")
