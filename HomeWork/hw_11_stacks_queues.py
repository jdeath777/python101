#Stacks Part starts from here

print("The name of stack is l1")

l1 = []

#using a function to do the list of operations

def stack(l1):
    for i in range(0,10):
        l1.append(i)
        print("size of stack is :", len(l1))
        print(l1)

    print('\n')
    print('\n')
    print("LIFO starts here")
    print('\n')
    for i in range(0,10):
        l1.pop()
        print("size of stack is:",len(l1))
        print(l1)

#Queues part starts from here        
    print('\n')
    print('\n')
    print('The queues start from here')
    print('\n')


    for i in range(0,10):
        l1.append(i)
        print('The size of the queue is', len(l1))
        print(l1)
    print('\n')
    print('\n')
    print('The LIFO method starts here: ')
    print('\n')
    for i in range(-10,0):
        l1.pop()
        print('The length of the queue is: ',len(l1))
        print(l1)


print(stack(l1))
