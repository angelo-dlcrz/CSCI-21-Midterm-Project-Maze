# Angelo B. Dela Cruz
# 222086
# October 9-11, 2022

# I have not discussed the Python language code in my program 
# with anyone other than my instructor or the teaching assistants 
# assigned to this course.

# I have not used Python language code obtained from another student, 
# or any other unauthorized source, either modified or unmodified.

# If any Python language code or documentation used in my program 
# was obtained from another source, such as a textbook or website, 
# that has been clearly noted with a proper citation in the comments 
# of my program.
def drawMaze(maze):
	print()
	for row in maze:
		for col in row:
			# Print function argument end=' ' instead of default '\n' so that there is only a
			# space instead of a new line between printed elements of the maze
			# Retrieved from https://docs.python.org/3/library/functions.html#print
			print(col, end=' ')
		print()

def updateMaze(maze_arr,row,col,chr):
	maze_arr[row][col] = chr
	return maze_arr

def setRow(y, lvl):
	if lvl == 1:
		return 2*(y // 3) + 1
	elif lvl == 2:
		return 2*(y // 4) + 1
	elif lvl == 3:
		return 2*(y // 5) + 1

def setCol(x, lvl):
	if lvl == 1:
		return 2*(x % 3) + 1
	elif lvl == 2:
		return 2*(x % 4) + 1
	elif lvl == 3:
		return 2*(x % 5) + 1

def chooseLevel(lvl):
	maze_1 = [
				['W','W','W','W','W','W','W'], 
				['W',' ','W',' ',' ',' ','W'],
				['W',' ','W',' ','W','W','W'],
				['W',' ',' ',' ',' ',' ','W'],
				['W',' ','W',' ','W','W','W'],
				['W',' ','W',' ',' ',' ','W'],
				['W','W','W','W','W','W','W']
			]

	maze_2 = [
				['W','W','W','W','W','W','W','W','W'], 
				['W',' ',' ',' ',' ',' ',' ',' ','W'], 
				['W',' ','W','W','W','W','W',' ','W'], 
				['W',' ',' ',' ',' ',' ','W',' ','W'], 
				['W',' ','W','W','W',' ','W','W','W'], 
				['W',' ','W',' ','W',' ',' ',' ','W'], 
				['W',' ','W',' ','W',' ','W',' ','W'], 
				['W',' ',' ',' ','W',' ','W',' ','W'], 
				['W','W','W','W','W','W','W','W','W'] 
			]

	maze_3 = [
				['W','W','W','W','W','W','W','W','W','W','W'], 
				['W',' ',' ',' ',' ',' ',' ',' ','W',' ','W'], 
				['W',' ','W','W','W',' ','W',' ','W',' ','W'], 
				['W',' ',' ',' ','W',' ','W',' ',' ',' ','W'], 
				['W','W','W',' ','W',' ','W',' ','W','W','W'], 
				['W',' ',' ',' ',' ',' ','W',' ',' ',' ','W'], 
				['W',' ','W',' ','W','W','W','W','W',' ','W'], 
				['W',' ','W',' ',' ',' ','W',' ','W',' ','W'], 
				['W',' ','W','W','W',' ','W',' ','W',' ','W'], 
				['W',' ',' ',' ','W',' ','W',' ',' ',' ','W'], 
				['W','W','W','W','W','W','W','W','W','W','W']
			]

	if lvl == 1:
		return maze_1
	elif lvl == 2:
		return maze_2
	elif lvl == 3:
		return maze_3

print("Welcome to the Maze!")
level = int(input("Select a level: 1, 2, or 3\n"))
start_point = int(input("Starting point: "))
end_point = int(input("Exit location: "))
maze = chooseLevel(level)
pos_row = setRow(start_point, level)
pos_col = setCol(start_point, level)
end_row = setRow(end_point, level)
end_col = setCol(end_point, level)
maze = updateMaze(maze,pos_row,pos_col,'O')
maze = updateMaze(maze,end_row,end_col,'X')

def checkPossibleDir(maze_list):
	pos_dir = []
	if maze_list[pos_row-1][pos_col] == ' ':
		pos_dir.append("North")
	if maze_list[pos_row][pos_col+1] == ' ':
		pos_dir.append("East")
	if maze_list[pos_row+1][pos_col] == ' ':
		pos_dir.append("South")
	if maze_list[pos_row][pos_col-1] == ' ':
		pos_dir.append("West")

	return pos_dir

while True:
	drawMaze(maze)
	maze = updateMaze(maze,pos_row,pos_col,' ')
	maze_arr = checkPossibleDir(maze)
	# The lower function returns a copy of the string where in all the cases of the characters are
	# converted to lowercase
	# Retrieved from https://docs.python.org/3/library/stdtypes.html#str.lower
	maze_lower = [i.lower() for i in maze_arr]
	print("Available Directions: ", end='')
	for i in maze_arr: print(i, end=' ')
	dir = input("\nWhich direction will you take?\n").lower()
	
	while True:
		# in here is used to check for membership of something within a sequence
		# Retrieved from https://docs.python.org/3/reference/expressions.html#in
		# in this case, it checks if the direction (str) is in the list containing all possible
		# directions
		if dir == "north" and "north" in maze_lower:
			pos_row -= 2
			break
		elif dir == "south" and "south" in maze_lower:
			pos_row += 2
			break
		elif dir == "east" and "east" in maze_lower:
			pos_col += 2
			break
		elif dir == "west" and "west" in maze_lower:
			pos_col -= 2
			break
		elif dir == "quit":
			print("\nTry again next time.")
			print("Goodbye.")
			# Keyword 'raise' is used to raise an exception or an error
			# Retrieved from https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement
			# SystemExit is an exception that allows us to exit the program
			# Retrieved from https://docs.python.org/3/library/exceptions.html#SystemExit
			raise SystemExit
		else:
			dir = input("\nPlease choose an available direction.\n").lower()
			continue
	maze = updateMaze(maze,pos_row,pos_col,'O')

	if pos_row == end_row and pos_col == end_col:
		drawMaze(maze)
		print("\nFound the exit!")
		print("Goodbye.")
		break
raise SystemExit