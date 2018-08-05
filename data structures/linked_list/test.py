from linked_list import LinkedList


my_list = LinkedList()

for i in range(0, 40):
	my_list.push_back(i)	


print("length")
print(my_list.length)
print("data")
print(my_list.get(1).data)
