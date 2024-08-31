class Node:
    def __init__ (self,data,int):
        self.data = data
        self.next = None
        
        
class Linked_list:
 def __init__(self):
        self.head= None
    
 def append (self,data:int):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      
    else:
      
         current = self.head
         while current.next:
               current = current.next
               current.next = new_node

 def findmax(self)->int:
    if self.head is None:
        return  None
    max_value = self.head.data
    current = self.head
    while current:
         if current.data> max_value:
            max_value = current.data
            current = current.next
        
        
    return max_value 
      
num = Linked_list()
num.append(3)
num.append(1)
num.append(5)
num.append(10)
print(num.find_max())
    

