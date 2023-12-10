#    Singly Linked list Q5
class Node:
    def __init__(self,data):
        self.data = data
        self.ref=None

class Linkedlist:
    def __init__(self):
        self.head = None
           # DISPLAY THE TOP OF THE NODE   
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"==>",end=" ")
                n = n.ref             
# FUNCTION FOR INSERTING A NEW VALUE OR NEW NODE AT FIRST POSITION 
    def add_begin(self, data):
        new_node= Node(data)
        new_node.ref = self.head    # ADD NEW NODE AS HEAD
        self.head = new_node          # MOVE THE HEAD TO POINT TO THE NEW NODE 
# ADD AT THE END
    def add_end(self,data):
        new_node= Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n= n.ref
            n.ref=new_node
    #ADD AT ANY POSITION
    def add_after(self, data,x):
        n = self.head
        while n is not None:
            if x ==n.data:
                break
            n=n.ref
        if n is None:
            print("node is not present in LL")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    #delete ar begin
    def delete_begin(self):
        if self.head is None:
            print("LL is empty so we can't delete nodes! ")  
        else:
            self.head=self.head.ref      
    
LL1=Linkedlist()
LL1.add_begin(50)
LL1.add_begin(30)
LL1.add_begin(10)
LL1.add_begin(45)
LL1.add_end(140)
LL1.add_after(400,140)
LL1.delete_begin()
LL1.display()
