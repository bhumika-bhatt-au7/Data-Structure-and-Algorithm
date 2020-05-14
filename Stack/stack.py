class stack:
    def __init__(self):
        self.items=[]

    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def view_stack(self):
        return self.items

    def is_empty(self):
        return self.items==[]

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

s=stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print(s.view_stack())
print(s.peek())
s.pop()
print(s.peek())
print(s.is_empty())
print(s.view_stack())

s.pop()
s.pop()
s.pop()
s.pop()

print(s.is_empty())
