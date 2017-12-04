import pdb
from stack import stack
from Class import *
##Taking the maze and turning it into a 2D array -------------------------------------------------------------
file = open("maze.txt", "r")

maze = []
temp = []

temp = file.read().splitlines()
#print temp
for i in temp:
	maze.append(list(i))
#print maze

file.close()

def dfs(maze, tracker, runner):
	start = maze.find_start() #find out why this isn't working as a coordinate
	start2 = Coordinates(start[0], start[1])
	runner.x_pos = maze.start_x
	runner.y_pos = maze.start_y
	tracker.push(start2)
	while (tracker.size() > 0):
		print tracker.top().x, tracker.top().y
		#print tracker.top().y
		#pdb.set_trace()
		runner.move(maze)
		if tracker.top().check_end(maze.maze):
			return
		maze.mark_maze(tracker.top())
		maze.print_maze()

def main(maze):
	Labryinth = Maze(maze)
	Labryinth.print_maze()
	tracker = PositionTracker()
	man = MazeRunner(0,0,tracker)
	dfs(Labryinth, tracker, man)
	
main(maze)

