# class Node:
#     def __init__(self,value):
#         self.data = value
#         self.next = None 


# class Stack:
#     def __init__(self):
#         self.top = None

#     def isempty(self):
#         return self.top == None


#     def push(self,value):
#         new_node = Node(value)

#         new_node.next = self.top
#         self.top = new_node


#     def peek(self):
#         if(self.isempty()):
#             return "Empty Stack"
#         else:
#             return self.top.data

#     def pop(self):
#         if(self.isempty()):
#             return "Empty Stack"
#         else:
#             self.top = self.top.next


#     def traverse(self):
#         temp = self.top 

#         while temp != None:
#             print(temp.data, end=' ')
#             temp = temp.next

    



# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(5)
# print(s.traverse())
# # print(s.isempty())
# print(s.peek())
# print(s.pop())
# print(s.traverse())


from collections import deque
stack = deque()

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

    def traverse(self):
        return self.container

def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)
    
    rstr = ''
    while stack.size()!=0:
        rstr += stack.pop()
    return rstr


def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2 


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch=='[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch==']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False
    return stack.size()==0

s = Stack()
s.push("We will conquere COVID-19")
# s.push(4)
# s.push(3)
# s.push(2)
# s.push(1)

# print(s.is_empty())
# print(s.pop())
# print(s.peek())
# print(s.size())
print(reverse_string("We will conquere COVI-19"))


print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("((a+g))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))