the_count = [1,2,3,4,5]

fruits = ['apples','oranges','pears','apricots']

change = [1,'pennies',2,'dimes',3,'quarters']


#this first loop goes through a list
for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")


for i in change:
    print(f"I got {i}")

elements = []


#using the range function to do 0 to 5 counts
for i in range(0,5):
    print(f"Adding {i} to the list.")
    #append is a function the list understands
    #it works as push
    elements.append(i)

for i in elements:
    print(f"Elements was: {i}")
