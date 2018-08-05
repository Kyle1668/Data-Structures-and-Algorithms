class LinkedList:

	class Node:
		def __init__(self, data):
			self.data = data
			self.next_node = None
			self.prev_node = None

	def __init__(self):
		self.length = 0
		self.head_node = None
		self.tail_node = None

	def push_back(self, data):

		new_node = self.Node(data)

		if (data != None):
			if (self.length == 0):
				self.head_node = self.tail_node = new_node
			else:
				self.tail_node.next_node = new_node
				new_node.prev_node = self.tail_node
				self.tail_node = new_node

			self.length += 1
			return True
		else:
			print("Can't Enter Null Value")
			return False


	def push_front(self, data):
		new_node = self.Node(data)

		if (self.length == 0):
			self.head_node = self.tail_node = new_node
			self.length = 1

	def get(self, index):
		print(str(index) + ":" + str(self.length))
        
		if (index < self.length):
			current_node = self.head_node

			for i in range(0, index - 1):
				print(str(i) + ":" + str(index))
				if (i == index):
					print(current_node.data)
					return current_node
				else:
					current_node = current_node.next_node
		else:
			print("Argued Index Greater Than Length")
			return None





