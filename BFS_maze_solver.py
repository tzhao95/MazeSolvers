import pdb
from stack import stack
from Class import *
from Fifo import Fifo

file = open("maze.txt", "r")

maze = []
temp = []

temp = file.read().splitlines()
for i in temp:
	maze.append(list(i))

file.close()

#def bfs(maze):
def check_adjacent(coord, maze, tracker):
	up = Coordinates(coord.x, coord.y - 1)
	left = Coordinates(coord.x-1, coord.y)
	down = Coordinates(coord.x, coord.y+1)
	right = Coordinates(coord.x+1, coord.y)
	if (maze.is_valid_pos(up)):
		tracker.append(up)
	if (maze.is_valid_pos(left)):
		tracker.append(left)
	if (maze.is_valid_pos(down)):
		tracker.append(down)
	if (maze.is_valid_pos(down)):
		tracker.append(down)

def print_tracker(tracker): #designed for trackers holding coordinates
	i = 0
	while(i < len(tracker)):
		print(i, "x:%d" % (tracker[i].x), "y:%d" % (tracker[i].y))
		i = i+1

def solve(maze, tracker):
	i = 1
	print_tracker(tracker)
	while (i > 0):
		#pdb.set_trace()
		if (tracker[i].check_end(maze.maze)):
			return
		check_adjacent(tracker[i], a, tracker)
		#print_tracker(tracker)
		if (maze.maze[tracker[i].y][tracker[i].x] != ' '):
			maze.maze[tracker[i].y][tracker[i].x] = 'Y'
		a.print_maze()
		pdb.set_trace()
		i = i + 1

i = 0
tracker = []
a = Maze(maze)
c = a.find_start()
end = Coordinates(5, 9)
random = Coordinates(15, 15)
#print(c, c.x, c.y)
tracker.append(c)
check_adjacent(tracker[i], a, tracker)
print_tracker(tracker)
a.print_maze()
a.mark_maze(random)
a.print_maze()
#tracker[i].check_end(a.maze)
#end.check_end(a.maze)
solve(a, tracker)
'''
def bfs(maze, list):
	while(list.size() > 0):
		if list.top().check_end(maze.maze):
			return
		up =  Coordinates(list.top().x, list.top().y-1)
		left = Coordinates(list.top().x-1, list.top().y)	
		down = Coordinates(list.top().x, list.top().y+1)
		right = Coordinates(list.top().x+1, list.top().y)
		if (maze.is_valid_pos(up)):
			list.push(up)
		if (maze.is_valid_pos(left)):
			list.push(left)
		if (maze.is_valid_pos(down)):
			list.push(down)
		if (maze.is_valid_pos(right)):
			list.push(right)
		maze.mark_maze(list.top())
		list.popf()
		list.shift()
		print (list.top().x)
		maze.print_maze()

def main(maze):
	a = Maze(maze)
	a.print_maze()
	tracker = Fifo()
	start = a.find_start()
	start2 = Coordinates(start[0], start[1])
	tracker.push(start2)
	bfs(a, tracker)

main(maze)
'''
