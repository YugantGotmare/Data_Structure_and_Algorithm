class Node:
    def __init__(self,value):
        self.data = value
        self.next = None 


class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top == None


    def push(self,value):
        new_node = Node(value)

        new_node.next = self.top
        self.top = new_node


    def peek(self):
        if(self.isempty()):
            return "Empty Stack"
        else:
            return self.top.data

    def pop(self):
        if(self.isempty()):
            return "Empty Stack"
        else:
            self.top = self.top.next


    def traverse(self):
        temp = self.top 

        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next

    



s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s.traverse())
# print(s.isempty())
print(s.peek())
print(s.pop())
print(s.traverse())


    