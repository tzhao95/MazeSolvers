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
		print list.top().x
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
