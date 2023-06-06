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
            data = self.top.data
            self.top = self.top.next
            return data


    def traverse(self):
        temp = self.top 

        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next


    def reverse_string(self, text):
        s = Stack()
        for i in text:
            s.push(i)
        res = ""
        while not s.isempty():
            res = res + s.pop()
        return res


stack = Stack()
print(stack.reverse_string('String'))