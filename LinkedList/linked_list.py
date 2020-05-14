class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=node()

    def append(self,data):
        new_node=node(data)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node

    def length(self):
        cur=self.head
        total_length=0
        while cur.next!=None:
            total_length+=1
            cur=cur.next
        return total_length

    def display(self):
        cur=self.head
        arr=[]
        while cur.next!=None:
            cur=cur.next
            arr.append(cur.data)    
        return arr

    def get_by_index(self,index):
        if index>=self.length():
            return "Index out of range" 
        cur=self.head
        cur_idx=0
        while True:
            cur=cur.next
            if cur_idx==index:
                return cur.data
            cur_idx+=1

    def delete_by_value(self,value):
        cur=self.head

        if cur and cur.data==value:
            self.head=cur.next
            cur=None
            return

        prev=None
        while cur and cur.data!=value:
            prev=cur
            cur=cur.next
        
        if cur is None:
            return
        prev.next=cur.next
        cur=None


    # 1=>2=>3=>4=>5=>null
    # 5=>4=>3=>2=>1=null

    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name + ":" + node.data)

    def reverse(self):
        prev=None
        cur=self.head
        while cur:
            nxt=cur.next
            cur.next=prev

            self.print_helper(prev, "PREV")
            self.print_helper(cur, "CUR")
            self.print_helper(nxt, "NXT")
            print("\n")

            
            prev=cur
            cur=cur.next
            cur=nxt
        self.head=prev

my_list=linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

print(my_list.length())
print(my_list.display())
# print(my_list.get_by_index(4))
# my_list.delete_by_value(1)
# print(my_list.display())
my_list.reverse()
print(my_list.display())