import collections

class Stack:

    def __init__(self):
        self.list = []

    def stack_op(self):
        for i in range(0,10):
            self.list.append(i)
            print("The elements in stack is: ", self.list)
            print(s.stack_len())
            print("The peak element is: ", self.peek())

    def stack_len(self):
        print("The length of the stack are: ",len(self.list))

    def peek(self):
        return self.list[len(self.list)-1]

    def pop(self):
        for i in range(0,10):
            self.list.pop()
            print(self.list)


s = Stack()
print(s.stack_op())
print("The element pooped is: ",s.pop())
