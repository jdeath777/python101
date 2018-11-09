import collections
import argparse
import sys

class Stack:
    list1=[]
    def __init__(self,s_list):
        self.list1 = s_list

    def stack_op(self):
        for i in range(len(self.list1)):
            print("The elements in the stack are: ",self.list1[i])

    def stack_len(self):
        print("The length of the stack is: ",len(self.list1))

    def peek(self):
        print("The element at the top is: ",self.list1[len(self.list1)-1])

    def pop(self):
        for i in range(len(self.list1)):
            print("The remaining element are: ")
            print("The popped element is: ",self.list1.pop())
            print("the remaining elements are: ", self.list1[i])



parser = argparse.ArgumentParser()
if sys.argv[1]=="--Stacks":
    parser.add_argument('--Stacks',type=str)
    args = parser.parse_args()
    li_list1 = args.Stacks.split(',')
    stacklist=[]
    for i in li_list1:
        stacklist.append(i)

s = Stack(stacklist)
s.stack_op()
s.peek()
s.pop()
s.stack_len()
