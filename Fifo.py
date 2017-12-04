'''
list = [1,2,3,4]
print list

list.append(1)
print list
print len(list)
''''''
def shift(list):
	i = 0
	while (i < len(list) - 1):
		list[i] = list[i+1]
		i = i+1
	list.pop()

def popf(list):
	list[0] = ""
'''
'''
list[0] = ""
print list
shift(list)
print list
'''

class Fifo():

	def __init__(self):
		self.list = []

	def push(self, var):
		self.list.append(var)

	def pop(self):
		self.list.pop()

	def top(self):
		i = len(self.list)
		return(self.list[i-1])

	def popf(self):
		self.list[0] = ""

	def shift(self):
		i = 0
		while ( i < len(self.list)-1):
			self.list[i] = self.list[i+1]
			i=i+1
		self.pop()

	def size(self):
		return len(self.list)
'''

fifo = fifoqueue()
fifo.push(1)
fifo.push(2)
fifo.push(3)
print fifo.list

fifo.pop()

print fifo.list
fifo.push(3)

fifo.popf()
print fifo.list

fifo.shift()
print fifo.list
'''