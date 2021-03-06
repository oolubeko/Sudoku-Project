#!/usr/bin/env python3
#Creator: Tomi Olubeko
#Date Created: 3/21/18
#Sudoku solver for a basic sudoku puzzle. A sudoku puzzle consists of 9 3x3 boxes containing the numbers 1 through 9 in each box.
#The objective of a sudoku puzzle is to place the numbers 1 to 9 in each of the boxes in such a way that no number is duplicated horizontally,
#vertically, or within each 3x3 box. The sudoku puzzle is solved when every box is filled with a number from 1 to 9 while fulfilling the 
#aforementioned constraints.

#The first step I will be taking is implementing methods to be able to construct a sudoku puzzle. I will be implementing this using a 2-dimensional
#array. An empty sudoku puzzle will be initialized as a 9x9 2-d array with all values initialized to 0, like so:

#											|0|0|0|0|0|0|0|0|0|
#											|0|0|0|0|0|0|0|0|0|
#											|0|0|0|0|0|0|0|0|0|
#											|0|0|0|0|0|0|0|0|0|
#											|0|0|0|0|0|0|0|0|0|
#											|0|0|0|0|0|0|0|0|0|
#											|0|0|0|0|0|0|0|0|0|
#											|0|0|0|0|0|0|0|0|0|
#											|0|0|0|0|0|0|0|0|0|


#######################################################################################################################################################

##########################################################Class for an empty sudoku puzzle#############################################################

#######################################################################################################################################################

#Ideas: Need to have a way to keep track of the boxes with immutable values. Possibly use an array or a hash map

class Sudoku:
	
	def __init__(self):
		self.grid = []		#Makes an empty array
		isSolved = False	#The solved variable is set to false by default
		for i in range(9):
			self.grid.append([])	#Populates the array with 9 arrays for the rows
		for i in range(9):
			for j in range(9):
				self.grid[i].append(0)	#Populates each row with 9 zeros
				
	#This method allows you to populate a row in the array. It takes in 2 parameters: The index of the row and an array containing the values needed to be 
	#Added in order. This method is mainly meant for building the puzzle before the actual solving starts.
	def add_row(self,row,arr):
		for i in range(9):
			self.grid[row][i] = arr[i]		#Puts the values contained in the array in the row of the sudoku puzzle.
			
	#This method allows you to add a specific item to a specific location. It takes in 3 parameters: The index of the row, the index of the column,
	#and the value needed to be added.
	def add(self,row,col,val):
		self.grid[row][col] = val
		
	#This method allows you to delete a specific item from a specific location. It takes in 2 parameters: The index of the row and the index of the column.
	def delete(self,row,col):
		self.grid[row][col] = 0		#Sets the value of the box to zero, effectively deleting the entry.
		
	#Override the string method for this class to print out a visual representation of the current state of the sudoku puzzle
	#										|0|0|0|0|0|0|0|0|0|
	#										|0|0|0|0|0|0|0|0|0|
	#										|0|0|0|0|0|0|0|0|0|
	#										|0|0|0|0|0|0|0|0|0|
	#										|0|0|0|0|0|0|0|0|0|
	#										|0|0|0|0|0|0|0|0|0|
	#										|0|0|0|0|0|0|0|0|0|
	#										|0|0|0|0|0|0|0|0|0|
	#										|0|0|0|0|0|0|0|0|0|

	def __str__(self):
		for i in range(9):
			print("|",end='')
			for j in range(9):
				print(self.grid[i][j],end='|')
			print()
		return ''
			
	#This method checks if Box1 meets the constraints for Sudoku and returns true if it does
	def check_box_one(self):
	
		#Possibility: we can optimize by only using one for loop that checks both row and col and uses offsets
		numArray = {}
		count = 0
		for i in range(3):
			for j in range(3):
				val = self.grid[i][j]
				if val in numArray:		#Check to see if the number is in the hash table, and if it is, increment its count by 1
					numArray[val] += 1
				else:
					numArray[val] = 1	#else, add it to the hash table
					
		#Iterate through the hash table and check if a value is greater than 1
		for key in numArray:
		
			if key == 0:		#We ignore zero values, because that is an unvisited square
				continue
			
			if numArray[key] > count:
				count = numArray[key]
				
		return count < 2
		
	#This method checks if Box2 meets the constraints for Sudoku and returns true if it does
	def check_box_two(self):
	
		#Possibility: we can optimize by only using one for loop that checks both row and col and uses offsets
		numArray = {}
		count = 0
		for i in range(3):
			for j in range(3,6):
				val = self.grid[i][j]
				if val in numArray:		#Check to see if the number is in the hash table, and if it is, increment its count by 1
					numArray[val] += 1
				else:
					numArray[val] = 1	#else, add it to the hash table
					
		#Iterate through the hash table and check if a value is greater than 1
		for key in numArray:
		
			if key == 0:		#We ignore zero values, because that is an unvisited square
				continue
			
			if numArray[key] > count:
				count = numArray[key]
				
		return count < 2
		
	#This method checks if Box3 meets the constraints for Sudoku and returns true if it does
	def check_box_three(self):
	
		#Possibility: we can optimize by only using one for loop that checks both row and col and uses offsets
		numArray = {}
		count = 0
		for i in range(3):
			for j in range(6,9):
				val = self.grid[i][j]
				if val in numArray:		#Check to see if the number is in the hash table, and if it is, increment its count by 1
					numArray[val] += 1
				else:
					numArray[val] = 1	#else, add it to the hash table
					
		#Iterate through the hash table and check if a value is greater than 1
		for key in numArray:
		
			if key == 0:		#We ignore zero values, because that is an unvisited square
				continue
			
			if numArray[key] > count:
				count = numArray[key]
				
		return count < 2
		
	#This method checks if Box4 meets the constraints for Sudoku and returns true if it does
	def check_box_four(self):
	
		#Possibility: we can optimize by only using one for loop that checks both row and col and uses offsets
		numArray = {}
		count = 0
		for i in range(3,6):
			for j in range(3):
				val = self.grid[i][j]
				if val in numArray:		#Check to see if the number is in the hash table, and if it is, increment its count by 1
					numArray[val] += 1
				else:
					numArray[val] = 1	#else, add it to the hash table
					
		#Iterate through the hash table and check if a value is greater than 1
		for key in numArray:
		
			if key == 0:		#We ignore zero values, because that is an unvisited square
				continue
			
			if numArray[key] > count:
				count = numArray[key]
				
		return count < 2
		
	#This method checks if Box5 meets the constraints for Sudoku and returns true if it does
	def check_box_five(self):
	
		#Possibility: we can optimize by only using one for loop that checks both row and col and uses offsets
		numArray = {}
		count = 0
		for i in range(3,6):
			for j in range(3,6):
				val = self.grid[i][j]
				if val in numArray:		#Check to see if the number is in the hash table, and if it is, increment its count by 1
					numArray[val] += 1
				else:
					numArray[val] = 1	#else, add it to the hash table
					
		#Iterate through the hash table and check if a value is greater than 1
		for key in numArray:
		
			if key == 0:		#We ignore zero values, because that is an unvisited square
				continue
			
			if numArray[key] > count:
				count = numArray[key]
				
		return count < 2
	
	#This method checks if Box6 meets the constraints for Sudoku and returns true if it does
	def check_box_six(self):
	
		#Possibility: we can optimize by only using one for loop that checks both row and col and uses offsets
		numArray = {}
		count = 0
		for i in range(3,6):
			for j in range(6,9):
				val = self.grid[i][j]
				if val in numArray:		#Check to see if the number is in the hash table, and if it is, increment its count by 1
					numArray[val] += 1
				else:
					numArray[val] = 1	#else, add it to the hash table
					
		#Iterate through the hash table and check if a value is greater than 1
		for key in numArray:
		
			if key == 0:		#We ignore zero values, because that is an unvisited square
				continue
			
			if numArray[key] > count:
				count = numArray[key]
				
		return count < 2
		
	#This method checks if Box7 meets the constraints for Sudoku and returns true if it does
	def check_box_seven(self):
	
		#Possibility: we can optimize by only using one for loop that checks both row and col and uses offsets
		numArray = {}
		count = 0
		for i in range(6,9):
			for j in range(3):
				val = self.grid[i][j]
				if val in numArray:		#Check to see if the number is in the hash table, and if it is, increment its count by 1
					numArray[val] += 1
				else:
					numArray[val] = 1	#else, add it to the hash table
					
		#Iterate through the hash table and check if a value is greater than 1
		for key in numArray:
		
			if key == 0:		#We ignore zero values, because that is an unvisited square
				continue
			
			if numArray[key] > count:
				count = numArray[key]
				
		return count < 2
		
	#This method checks if Box8 meets the constraints for Sudoku and returns true if it does
	def check_box_eight(self):
	
		#Possibility: we can optimize by only using one for loop that checks both row and col and uses offsets
		numArray = {}
		count = 0
		for i in range(6,9):
			for j in range(3,6):
				val = self.grid[i][j]
				if val in numArray:		#Check to see if the number is in the hash table, and if it is, increment its count by 1
					numArray[val] += 1
				else:
					numArray[val] = 1	#else, add it to the hash table
					
		#Iterate through the hash table and check if a value is greater than 1
		for key in numArray:
		
			if key == 0:		#We ignore zero values, because that is an unvisited square
				continue
			
			if numArray[key] > count:
				count = numArray[key]
				
		return count < 2
		
	#This method checks if Box9 meets the constraints for Sudoku and returns true if it does
	def check_box_nine(self):
	
		#Possibility: we can optimize by only using one for loop that checks both row and col and uses offsets
		numArray = {}
		count = 0
		for i in range(6,9):
			for j in range(6,9):
				val = self.grid[i][j]
				if val in numArray:		#Check to see if the number is in the hash table, and if it is, increment its count by 1
					numArray[val] += 1
				else:
					numArray[val] = 1	#else, add it to the hash table
					
		#Iterate through the hash table and check if a value is greater than 1
		for key in numArray:
		
			if key == 0:		#We ignore zero values, because that is an unvisited square
				continue
			
			if numArray[key] > count:
				count = numArray[key]
				
		return count < 2
		
			
	#This method checks if a particular box fulfills the rules of sudoku. That is, the numbers 1 to 9 appear uniquely in the 3x3 box. 
	#This method takes in 2 parameters: The row and the col, and returns a boolean value based on if the box fulfills the sudoku rules
	def check_box(self,row,col):
		#val = self.grid[row][col]
		isValid = True
		
		#Get the Box number: Box 1: [0][0] to [2][2], Box 2: [0][3] to [2][5], Box 3: [0][6] to [2][8]
		#Box 4: [3][0] to [5][2], Box 5: [3][3] to [5][5], Box 6: [3][6] to [5][8]
		#Box 7: [6][0] to [8][2], Box 8: [6][3] to [8][5], Box 9: [6][6] to [8][8]
		
		if row == 0 or row == 1 or row == 2:	#Case for Box 1-3
			if col == 0 or col == 1 or col == 2:	#Box 1
				isValid = self.check_box_one()
				
			elif col == 3 or col == 4 or col == 5:	#Box 2
				isValid = self.check_box_two()
				
			elif col == 6 or col == 7 or col == 8:	#Box 3
				isValid = self.check_box_three()
				
		elif row == 3 or row == 4 or row == 5:	#Case for Box 4-6
			if col == 0 or col == 1 or col == 2:	#Box 4
				isValid = self.check_box_four()
				
			elif col == 3 or col == 4 or col == 5:	#Box 5
				isValid = self.check_box_five()
				
			elif col == 6 or col == 7 or col == 8:	#Box 6
				isValid = self.check_box_six()
				
		elif row == 6 or row == 7 or row == 8:	#Case for Box 7-9
			if col == 0 or col == 1 or col == 2:	#Box 7
				isValid = self.check_box_seven()
				
			elif col == 3 or col == 4 or col == 5:	#Box 8
				isValid = self.check_box_eight()
				
			elif col == 6 or col == 7 or col == 8:	#Box 9
				isValid = self.check_box_nine()
				
		return isValid
		
	#This method checks if the row of the value is unique. One parameter: The row
	def check_row(self,row):
		h_row = {}
		count = 0
			
		for i in range(9):
			if self.grid[row][i] in h_row:
				h_row[self.grid[row][i]] += 1
			else:
				h_row[self.grid[row][i]] = 1
			
		for key in h_row:
			if key == 0:
				continue
			if h_row[key] > count:
				count = h_row[key]
					
		return count < 2
			
	#This method checks if the col of the value is unique. One parameter: The col
	def check_col(self,col):
		v_col = {}
		count = 0
			
		for i in range(9):
			if self.grid[i][col] in v_col:
				v_col[self.grid[i][col]] += 1
			else:
				v_col[self.grid[i][col]] = 1
		
		for key in v_col:
			if key == 0:
				continue
			if v_col[key] > count:
				count = v_col[key]
					
		return count < 2
			
#####################The solver method that will call all the methods made previously. It consists of three steps:###################################
#####################1. Enumerate all empty cells from left to right, top to bottom.#################################################################
#####################2. Our "current cell is the first cell in the enumeration#######################################################################
#####################3. Enter a 1 into the current cell. If it violates the sudoku condition, try entering a two, then a three, and so on until:#####
##########################a. The entry does not violate the sudoku condition or #####################################################################
##########################b. You have reached nine and still violate the sudoku condition############################################################
#####################4. In case a: If the current cell was the last enumerated one, then the puzzle is solved. If not, then go back to step 2 with ##
#########################the next cell in the enumerated cells#######################################################################################
########################In case b: If the current cell is the first cell in the enumeration, then the sudoku puzzle does not have a solution.########
########################If it is not, then erase the 9 from the current cell, call the previous cell in the enumeration current, and continue with #3

	def solve(self):
	
	#Enumerate all empty cells in typewriter format
		unSolvable = False
		empty_squares = []
		for i in range(9):
			for j in range(9):
				val = self.grid[i][j]
				t = i, j		#store the coordinate as a tuple in the list of empty spaces
				if val == 0:
					empty_squares.append(t)
					
		current = 0
		while current < len(empty_squares) and not unSolvable:
			coord = empty_squares[current]	#Get the values for the row and col
			row = coord[0]
			col = coord[1]
			
			if self.grid[row][col] >= 9:
				self.delete(row,col)		#Check for backtracking, and the value is already 9
				current -= 1
				continue
				
			self.grid[row][col] += 1	#Increment the value in the row and col by 1
			
			h_Valid = self.check_row(row) 	#Holds the boolean value for if the row fulfills sudoku rules
			v_Valid = self.check_col(col)	#Holds the boolean value for if the col fulfills sudoku rules
			b_Valid = self.check_box(row, col)	#Checks if the box fulfills sudoku rules
			
			while not h_Valid or not v_Valid or not b_Valid:		#Increments the value in the square by one if the rules of sudoku are not met
				if row == 0 and col == 0 and self.grid[row][col] == 9:		#Case where there is no solution to the sudoku puzzle
					unSolvable = True
					break
				
				elif self.grid[row][col] >= 9:			#The current cell still violates the sudoku condition and is at nine, so go back to the previous current
					self.delete(row,col)	#Erase 9 from the cell
					current -= 1			#Go back one cell and update that value
					break
				
				self.grid[row][col] += 1
				h_Valid = self.check_row(row)
				v_Valid = self.check_col(col)
				b_Valid = self.check_box(row, col)
			
			#print(self)
			
			if self.grid[row][col] != 0:
				current += 1
			

		if unSolvable:
			return
			
		else:
			self.isSolved = True
			

def main():
	sudoku = Sudoku()
	print(sudoku)
	sudoku.add_row(0,[8,0,0,0,1,6,0,0,9])
	sudoku.add_row(1,[0,2,0,0,0,4,5,1,0])
	sudoku.add_row(2,[0,3,5,0,7,0,4,0,0])
	sudoku.add_row(3,[5,1,0,4,0,3,0,0,0])
	sudoku.add_row(4,[7,0,2,0,5,0,1,0,3])
	sudoku.add_row(5,[0,0,0,7,0,1,0,5,8])
	sudoku.add_row(6,[0,0,7,0,9,0,8,2,0])
	sudoku.add_row(7,[0,5,8,3,0,0,0,6,0])
	sudoku.add_row(8,[9,0,0,2,6,0,0,0,5])
	print(sudoku)
	sudoku.solve()
	print(sudoku)

main()
			
			

			
			
			
			