class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_end(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
			return
		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node

	def print_list(self):
		current = self.head
		while current:
			print(current.data, end=" ")
			current = current.next
		print()

linked_list = LinkedList()

linked_list.insert_at_end(3)
linked_list.insert_at_end(7)
linked_list.insert_at_end(10)


print("Linked list after insertion at the end:")
linked_list.print_list()
