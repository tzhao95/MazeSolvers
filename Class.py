from stack import stack
import pdb

class Maze():
	def __init__(self, maze): #the maze must be a 2D array
		self.maze = maze
		self.max_x = len(maze[0]) - 1
		self.max_y = len(maze) - 1
		self.start_x = 0
		self.start_y = 0

	def is_valid_pos(self, coordinate)	:
		return coordinate.x >= 0 and coordinate.x <= self.max_x and coordinate.y >= 0 and coordinate.y <= self.max_y and (self.maze[coordinate.y][coordinate.x] == " " or self.maze[coordinate.y][coordinate.x] == "B")

	def find_start(self):
		a = 0
		b = 0
		for x in self.maze:
			for y in x:
				if self.maze[b][a] == 'A':
					sX = a
					self.start_x = a
					sY = b
					self.start_y = b
					return [sX, sY] #since this is here, I should just make it return a coordinate
				a += 1
			b += 1
			a = 0

	def print_maze(self):
		a = 0
		b = 0
		for row in self.maze:
			for col in row:
				print self.maze[b][a],
				a += 1
			b += 1
			a = 0
			print " "

	def mark_maze(self, coordinate):
		self.maze[coordinate.y][coordinate.x] = "Y"

####Test maze to make sure the code works#########################################

file = open("maze.txt", "r")
maze = []
temp = []
temp = file.read().splitlines()
for i in temp:
	maze.append(list(i))

file.close()
########################################################################################
class Coordinates():
	def __init__(self, x, y):
		self.x = x #current x coordinate
		self.y = y #current y coordinates

	def check_end(self, maze): #check to see if coordinates meet end condition assuming end condition is the space is 'B'
		if maze[self.y][self.x] == "B":
			print "COMPLETE! BITCH!"
			print self.x, self.y
			return True

########################################################################################
class PositionTracker(stack):
	def __init__(self):
		self.list = []

	def plush(self, n):
		self.push(n)

	def back_up(self):
		self.pop()

#########################################################################################
class MazeRunner():

	def __init__(self, x_pos, y_pos, tracker):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.tracker = tracker  #the tracker is the stack that it will store its position and look for its current position

	def add_possible_moves(self, maze): #self knows current position, maze to look through maze, Returns which way you can go or if you should pop
		up = Coordinates(self.x_pos, self.y_pos - 1)
		#pdb.set_trace()
		left = Coordinates(self.x_pos - 1, self.y_pos)
		#pdb.set_trace()
		down = Coordinates(self.x_pos, self.y_pos + 1)
		#pdb.set_trace()
		right = Coordinates(self.x_pos + 1, self.y_pos)
		if (maze.is_valid_pos(up)):
			self.tracker.push(up)
			return 1
		if (maze.is_valid_pos(left)):
			self.tracker.push(left)
			return 2
		if (maze.is_valid_pos(down)):
			self.tracker.push(down)
			return 3
		if (maze.is_valid_pos(right)):
			self.tracker.push(right)
			return 4	

	def move(self, maze): #pos is a coordinate and maze is a Maze
		dir = self.add_possible_moves(maze)
		#print dir
		if dir == 1:
			self.x_pos = self.tracker.top().x
			self.y_pos = self.tracker.top().y
			#maze.mark_maze(self.tracker.top())
			print "up"
			return True
		if dir == 2:
			self.x_pos = self.tracker.top().x
			self.y_pos = self.tracker.top().y
			print "left"
			return True
		if dir == 3:
			self.x_pos = self.tracker.top().x
			self.y_pos = self.tracker.top().y
			print "down"
			return True
		if dir == 4:
			self.x_pos = self.tracker.top().x
			self.y_pos = self.tracker.top().y
			print "right"
			return True
		else:
			self.tracker.pop()
			self.x_pos = self.tracker.top().x
			self.y_pos = self.tracker.top().y
			print "Backed Up"
			return False

