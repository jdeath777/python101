#implementing stack

stack = input("Enter the name to be added: ")

lst = stack.split(' ')


b = input("Enter the new name to be added: ")

c = lst.append(b)

print(lst)

i  = input("do you want to pop the item: ")

if(i == 'y' or i == 'Y'):
    lstack = ["Amar", "Akbar", "Anthony"]
    p = lst.pop()
    print("The popped item is: ",p)
    print("The remaining item is: ")
    print(lst)
else:
    print(lst)
