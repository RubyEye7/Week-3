import random

class MyQueue:

    def __init__(self):
        self.my_list = []


    def push(self, x):
        self.my_list.append(x)
        return self.my_list

    def pop(self):
        if len(self.my_list) > 0:
            popped = self.my_list[0]
            self.my_list = self.my_list[1:]
            return popped

    def peek(self):
        if len(self.my_list) > 0 :
            peeked = self.my_list[0]
            return peeked

    def empty(self):
        if len(self.my_list) == 0:
            return empty
        else:
            return empty


obj = MyQueue()
obj.push(random.randint(1,30))
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
