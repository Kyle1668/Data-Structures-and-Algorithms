class LinkedList:

	def __init__(self):
		self.length = 0 
		self.head_node = None
		self.tail_node = None

	def init_node(self, data):
		return {
			"data": data,
			"prev_node": None,
			"next_node": None
		}
	
	def push_back(self, data):

		new_node = self.init_node(data) 

		if (data != None):			
			if (self.length == 0):
				self.head_node = self.tail_node = new_node
				self.length += 1
			else:
				self.tail_node["next_node"] = new_node
				new_node["prev_node"] = self.tail_node
				self.tail_node = new_node
			
			self.length += 1
			return True
		else:
			print("Can't Enter Null Value")
			return False


	def get(self, index):
		if (index < self.length):
			current_node = self.head_node

			for i in range(0, index):
				if (i == index):
					return current_node 
				else:
					current_node = current_node["next_node"]

		else:
			print("Argued Index Greater Than Length")
			return None
		




