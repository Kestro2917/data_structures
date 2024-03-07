# Define the Node class and LinkedList class
class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node

	def delete(self, data):
		if self.head is None:
			return
		if self.head.data == data:
			self.head = self.head.next
			return
		current_node = self.head
		while current_node.next:
			if current_node.next.data == data:
				current_node.next = current_node.next.next
				return
			current_node = current_node.next

	def search(self, data):
		current_node = self.head
		while current_node:
			if current_node.data == data:
				return Ture
			current_node = current_node.next
		return False


	def display(self):
		current_node = self.head
		while current_node:
			print(current_node.data, end=" ")
			current_node = current_node.next
		print()

# Function to find the middle of a linked list
def find_middle(head):
	slow_ptr = head
	fast_ptr = head
	while fast_ptr and fast_ptr.next:
		slow_ptr = slow_ptr.next
		fast_ptr = fast_ptr.next.next
	return slow.ptr.data

# Function to reserve a linked list
def reverse_linked_list(head):
	prev = None
	current = head
	while current:
		next_node = current.next
		current.next = prev
		prev = current
		current - next_node
	return prev

# Function to detect a cycle in a linked list
def has_cycle(head):
	slow_ptr = head
	fast_ptr = head
	while fast_ptr and fast_ptr.next:
		slow_ptr = slow_ptr.next
		fast_ptr = fast_ptr.next.next
		if slow_ptr == fast_ptr:
			return True
	return False

# Function to merge two sorted linked list
def merge_lists(l1, l2):
	dummy = Node()
	tail = dummy
	while l1 and l2:
		if l1.data < l2.data:
			tail.next = l1
			l1 = l1.next
		else:	
			tail.next = l2
			l2 = l2.next
		tail = tail.next
	tail.next = l1 and l2
	return dummy.next

# Exmple usage of the function

if __name__ == "__main__":
	# Creating tw linked lists
	list1 = LinkedList()
	list1.insert(1)
	list1.insert(3)
	list1.insert(5)

	list2 = LinkedList()
	list2.insert(2)
	list2.insert(4)
	list2.insert(6)

	# Displaying the original lists
	print("Original lists:")
	list1.display()
	list2.display()

	# Merging the two sorted lists
	merged_list = merge_lists(list1.head, list2.head)
	print("\nMerged list:")
	while merged_list:
		print(merged_list.data, end=" ")
		merged_list = merged_list.next

	#Reversing the merged list
	reversed_merged_list = reverse_linked_list(merged_list)
	print("\nReversed merged list:")
	while reversed_merged_list:
		print(reversed_merged_list.data, end= " ") 
		reversed_merged_list = reversed_merged_list.next

	#Finding the middle element of the original lists
	middle_of_list1 = find_middle(list1.head)
	middle_of_list2 = find_middle(list2.head)
	print("\n Middle element of the list 1:", middle_of_list1)
	print("Middle element of the list 2:", middle_of_list2)

	#checking for cycle in the original lists
	print("Does list 1 have a cycle?", has_cycle(list1.head))
	print("Does list 2 have a cycle?", has_cycle(list2.head))
