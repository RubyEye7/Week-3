import random

class MyStack:

    def __init__(self):
        self.my_list = []


    def push(self, x):
        self.my_list.append(x)
        return self.my_list
        print(self.my_list)

    def pop(self):
        if len(self.my_list) > 0:
            popped = self.my_list[-1]
            self.my_list = self.my_list[:len(self.my_list)-2]
            return popped

    def peek(self):
        if len(self.my_list) > 0:
            peeked = self.my_list[-1]
            return peeked

    def empty(self):
        if len(self.my_list) == 0:
            empty = True
        else:
            empty = False
        return empty


obj = MyStack()
Queue_Operator = input("Would you like to 1.Push a new number, 2.Pop the most recent, 3.Peek the most recent, or 4.Check if the stack is empty:  ")
if Queue_Operator == "1":
    obj.push()
if Queue_Operator == "2":
    obj.pop()
if Queue_Operator == "3":
    obj.peek()
if Queue_Operator == "4":
    obj.empty()


param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
