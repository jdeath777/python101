import collections
import argparse
import sys
from collections import deque

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
            print("the remaining elements are: ", self.list1[i])



class Queue:
    list1=[]
    de =[]

    
    def __init__(self,s_list):
        self.list1 = s_list
        self.de = collections.deque(self.list1)

    def enque(self):
        for i in range(len(self.list1)):
            print("The elements in queue are: ", self.list1[i])

    def queue_len(self):
        print("The length of the queue are: ",len(self.list1))

    def deque(self):
        for i in range(len(self.list1)):
            print("The poped element is :",self.de.popleft())


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

else:
    parser.add_argument('--Queues',type=str)
    args = parser.parse_args()
    li_list1 = args.Queues.split(',')
    queuelist = []
    for i in li_list1:
        queuelist.append(i)
        q = Queue(queuelist)
        q.enque()
        q.deque()
        q.queue_len()
