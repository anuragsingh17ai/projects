#stack is a data structure that follow lifo
stack=[] #using list as stack
def push(data):
    stack.append(data)

def Pop():
    return stack.pop() if len(stack)>0 else print("stack is empty")

def isEmpty():
    return len(stack)==0

def peek():
    return stack[-1]

while(True):
    print("Select the operation 1.push 2.pop 3.isempty ")

