class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=node()

    def add(self,data):
        new_node=node(data)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node

    def length(self):
        total=0
        cur=self.head
        while cur.next!=None:
            cur=cur.next
            total+=1
        return total  
     
    def find_value(self,index):
        if index>self.length():
            return "Out of range"
        cur=self.head
        idx=0
        while cur.next!=None:
            cur=cur.next   
            if index==idx:
            
                return cur.data
           
            idx += 1
            
    def remove_by_index(self,index):
        if index>self.length():
            return "Out of range"
        cur=self.head
        idx=0
        while cur.next!=None:
            if index==idx:
                cur.next=cur.next.next
            cur=cur.next
            idx+=1
           

    def display(self):
        arr=[]
        cur=self.head
        while cur.next!=None:
            cur=cur.next
            arr.append(cur.data)
            
        return arr

my_list=linked_list()
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(4)
my_list.add(5)

print(my_list.display())
print(my_list.length())
print(my_list.find_value(3))
# my_list.remove_value(3)
my_list.remove_by_value(3)
print(my_list.display())

