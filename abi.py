class Node: 

 # Function to initialise the node object 
 def __init__(self, data):
    self.data = data # Assign data 
    self.next = None # Initialize next as null 


# Linked List class contains a Node object 
class LinkedList: 

 # Function to initialize head 
 def __init__(self): 
    self.head = None


 # Functio to insert a new node at the beginning 
 def push(self, new_data): 
    new_node = Node(new_data) 
    new_node.next = self.head 
    self.head = new_node 



 def insertAfter(self, prev_node, new_data): 

  # 1. check if the given prev_node exists 
    if prev_node is None: 
        print ("The given previous node must inLinkedList.")
        return

  
    new_node = Node(new_data) 

  # 4. Make next of new Node as next of prev_node 
    new_node.next = prev_node.next

  # 5. make next of prev_node as new_node 
    prev_node.next = new_node 



 def append(self, new_data): 
    new_node = Node(new_data) 
    if self.head is None: 
        self.head = new_node 
    return
    last = self.head 
    while (last.next): 
        last = last.next

  # 6. Change the next of last node 
    last.next = new_node 


 # Utility function to print the linked list 
 def printList(self): 
    temp = self.head 
    while (temp): 
        print (temp.data, end=" " )
        temp = temp.next



# Code execution starts here 
if __name__=='__main__': 
    

 # Start with the empty list 
    llist1 = LinkedList() 
    llist2 = LinkedList()
    llist3 = LinkedList()
 # Insert 6. So linked list becomes 6->None 
    llist1.push('6x2')
    llist1.push('4x1') 
     
    
    llist2.push('6x2')
    llist2.push('5x1') 
    
#  # Insert 7 at the beginning. So linked list becomes 7->6->None 
#     llist1.push(7); 

#  # Insert 1 at the beginning. So linked list becomes 1->7->6->None 
#     llist1.push(1); 

#  # Insert 4 at the end. So linked list becomes 1->7->6->4->None 
#     llist1.append(4) 

#  # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None 
#     llist1.insertAfter(llist1.head.next, 8) 
    temp=llist1.head
    temp1=llist2.head
   
    while temp1 and temp:
        x=temp.data 
        s=temp1.data 
        y=x.split("x")
        z=s.split("x")
        if y[1]==z[1]:
            num=int(y[0])+int(z[0])
            f=str(num)+"x"+y[1]
            llist3.push(f)
        temp = temp.next
        temp1=temp1.next
    llist3.printList() 
     

# This code is contributed by Manikantan Narasimhan