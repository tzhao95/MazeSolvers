class stack():

	def __init__(self):
		self.list = []

	def push(self, var):
		self.list.append(var)

	def pop(self):
		self.list.pop()

	def top(self):
		i=len(self.list)
		return(self.list[i-1])

	def size(self):
		return len(self.list)

s = stack()
print s.size()
s.push(1)
s.push(2)
s.push(3)
print (s.list)

s.pop()

print (s.list)

print (s.top())

print s.size()