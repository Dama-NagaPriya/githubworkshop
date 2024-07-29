class Node:
	
	def __init__(self,data):

		self.__data = data
		self.__next = None		

	def set_data(self,data):
		self.__data = data

	def get_data(self):
		return self.__data

	def set_next(self,next):
		self.__next = next

	def get_next(self):
		return self.__next



class CircularLinkedList:

	def __init__(self):
		self.__head = None


	def add_at_head(self,element):

		# Create a new node
		n = Node(element)	

		# Check if the list does not exist or not
		if self.__head == None:
		    
			# Set the next reference to the same node
			n.set_next(n)
			self.__head = n			
			
		else:
		# Check if the list already exist
		
			# Traverse till the end of the list
			q = self.__head
			while q.get_next() != self.__head:
				q = q.get_next()
				
			# Attach the node
			n.set_next(self.__head)
			
			# Set head to the newly created node
			self.__head = n
			
			# Set the next reference of the last node to head
			q.set_next(self.__head)
			
		print("Node added @ head")		
		
		


	def add_at_tail(self,element):
	    
		# Create a new node
		n = Node(element)	
		
		# Check if the list does not exist or not
		if self.__head == None:
		    
			# Set the next reference to the same node
			n.set_next(n)
			self.__head = n			
			
		else:
			# Check if the list already exist
			# Traverse till the end of the list
			q = self.__head
			while q.get_next() != self.__head:
				q = q.get_next()
				
			# Set the next reference of the newly created node
			q.set_next(n)
			
			# Attach the node
			n.set_next(self.__head)					
			
		print("Node added @ tail")		
		
		
	def delete_node(self,element):
		
		# Case (i) If the list does not exist
		
		if self.__head == None:
		    
			print("No nodes available")
			return # Gets out of the method
			
		# Case (ii) If there exists only one node and that is to be deleted
		
		if self.__head.get_data() == element and self.__head.get_next() == self.__head:
		    
			# Dereference head and leave the object to be garbage collected
			
			self.__head = None
			
			print("Node successfully deleted !")
			
			return 
			
		# Case (iii) If there are multiple nodes and the first node is to be deleted.
		
		if self.__head.get_data() == element and self.__head.get_next() != self.__head:
		    
			# Set a reference to the last node.
			
			q = self.__head
			
			while q.get_next() != self.__head:
				q = q.get_next()
				
			# Set a reference variable to the first node
			p = self.__head
			
			# Move head to the next node.
			self.__head = self.__head.get_next()
			
			# Break the link of the node to be deleted
			p.set_next(None)
			
			# Set the next reference of the last node to the newly pointed head
			q.set_next(self.__head)
			
			# Dereference p and leave the object to be garbage collected
			p = None
			
			print("Node has been deleted")
			
			return
			
		# Case (iv) Delete a node in between
		
		# Search for the node
		found = False
		q = self.__head
		k = q
		
		while q.get_next() != self.__head:
			
			if q.get_data() == element:
				found = True
				break
				
			k = q
			q = q.get_next()
			
		# Check if it is the last node
		
		if q.get_data() == element:
		    
			found = True
			
		# Check if the node has been found
		if found:
		    
			# Maintain the links
			k.set_next(q.get_next())
			
			# Break the link of the node to be deleted
			q.set_next(None)
			
			# Dereference q and leave the object to be garbage collected
			q = None
			
			print("Node in between has been deleted !")
			
		else:
			print("Not could not be located")
			
			
	def count_nodes(self):
	    
		q = self.__head
		counter = 0
		
		while q.get_next() != self.__head:
			counter += 1
			q = q.get_next()
			
		counter += 1
		
		print("Total nodes : "+str(counter))
			

	def display_nodes(self):
		
		if self.__head == None:
			print("List is empty")
		else:
			p = self.__head
			while p.get_next() != self.__head:
				#print(p.get_data(), end = "  ")
				print("["+str(p.get_data())+"|"+str(p.get_next())+"]", end = "     " )
				p = p.get_next()
				
			print("["+str(p.get_data())+"|"+str(p.get_next())+"]", end = "     " )
				
				
				
cll = CircularLinkedList()
while True:
	print("\nMenu")
	print("----")
	print("1. Add @ Head")
	print("2. Display")
	print("3. Add @ Tail")
	print("4. Delete Node")
	print("5. Count nodes")
	print("6. Exit")
	print("Choose an option")
	opt = int(input())
	
	if opt == 1:
		print("Enter element to add")
		n = int(input())
		cll.add_at_head(n)
	elif opt == 2:
		cll.display_nodes()
	elif opt == 3:
		print("Enter element to add")
		n = int(input())
		cll.add_at_tail(n)
	elif opt == 4:
		print("Enter element to delete")
		n = int(input())
		cll.delete_node(n)
	elif opt == 5:
		cll.count_nodes()
	else:
		break
