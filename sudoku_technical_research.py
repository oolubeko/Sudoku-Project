#Sudoku Project Take 1
#1/13/2018 1:49 A.M
#Building classes/functions I think I will need for the sudoku solver

'''
#Box class for each of the nine sudoku boxes
class Box(object):
	#Creates an empty box: A 2-d array, with three elements, each element an array containing three elements
	def __init__(self):
		self.box = []
		for i in range(3):
			self.box.append([0,0,0])
'''

#Grid class for the whole sudoku grid. 
class Grid():
	#Creates a 2-d array of a 9x9 grid
	def __init__(self):
		self.grid = []
		for i in range(9):
			self.grid.append([0,0,0,0,0,0,0,0,0])

	def add_row_n(self,n,array_to_add):
		for i in range(9):
			self.grid[n][i] = array_to_add[i]

	def add_num(self,num,row,col):
		self.grid[row][col] = num

	def remove(self,row_in_box,col_in_box):
		if self.grid[box_num][row_in_box][col_in_box] != 0:
			self.grid[row_in_box][col_in_box] = 0

	#Checks to see whether a particular entry into a box fits sudoku horizontal rules
	#Checks whether all horizontal entries in that row are unique
	def validate_horizontal(self,row_in_box,col_in_box):
		num = self.grid[row_in_box][col_in_box]
		if num == 0:
			return True
		for i in range(9):
			if i == col_in_box:
				continue
			if self.grid[row_in_box][i] == num:
				return False
		return True

	#Checks whether a particular entry into a box fits sudoku vertical rules
	#Checks whether all vertical entries in that column are unique
	def validate_vertical(self,row_in_box,col_in_box):
		num = self.grid[row_in_box][col_in_box]
		if num == 0:
			return True
		for i in range(9):
			if i == row_in_box:
				continue
			if self.grid[i][col_in_box] == num:
				return False
		return True

	#Gets the row and col of a particular entry and returns which 3x3 box the entry belongs to
	#Boxes are labeled from 1 to 9 from left to right, top to bottom

	#Checks whether a particular entry into a box fits sudoku 3x3 box rules
	#Checks to see if for the 3x3 box the entry belongs to, it is unique
	def validate_box(self,row_in_box,col_in_box):


	def __str__(self):
		print('' + '_' * 37)
		for i in range(len(self.grid)):
			#print(' ' + '_' * 36)
			for j in range(len(self.grid[0])):
				if j == 0:
					print('|_' + str(self.grid[i][j]) + '_', end='')
					continue
				if j == 8:
					print('|_' + str(self.grid[i][j]) + '_',end='|\n')
					continue
				print('|_' + str(self.grid[i][j]) + '_', end='')
			#print()
		#print('' + '-' * 37)
		return ''


def main():
	sudoku = Grid()
	print(sudoku)
	sudoku.add_row_n(0,[8,0,0,5,0,0,3,7,6])
	sudoku.add_row_n(1,[1,0,0,0,0,3,0,5,0])
	sudoku.add_row_n(2,[0,0,5,7,0,0,0,2,0])
	sudoku.add_row_n(3,[0,5,7,0,0,0,0,0,3])
	sudoku.add_row_n(4,[0,6,9,0,8,0,4,1,0])
	sudoku.add_row_n(5,[3,0,0,0,0,0,5,6,0])
	sudoku.add_row_n(6,[0,1,0,0,0,4,7,0,0])
	sudoku.add_row_n(7,[0,9,0,8,0,0,0,0,5])
	sudoku.add_row_n(8,[6,4,2,0,0,7,0,0,1])
	print(sudoku)

main()



