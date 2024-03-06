class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_beginning(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def print_list(self):
		current = self.head
		while current:
			print(current.data, end= " ")
			current = current.next
		print()

linked_list = LinkedList()

linked_list.insert_at_beginning(3)
linked_list.insert_at_beginning(7)
linked_list.insert_at_beginning(10)


print("Linked list after insertion at the beginning:")
linked_list.print_list()

