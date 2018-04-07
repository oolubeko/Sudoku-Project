import java.util.Scanner;
import java.util.ArrayList;

//Implementation of the sudoku solver using java. 
public class Grid {
	
	private int[][] grid = new int[9][9];
	private boolean isSolved = false;
	
	//The constructor initializes an empty 9x9 2d array
	public Grid() {
		for(int i = 0; i < 9; i++) {
			for(int j = 0; j < 9; j++) {
				this.grid[i][j] = 0;
			}
		}
			
	}
	
	public boolean getStatus() {
		return this.isSolved;
	}
	
	//Helper method to convert a string of numbers to an array
	private int[] stringToNum(String s) {
		int[] arr = new int[9];
		for(int i = 0; i < s.length();i++) {
			char c = s.charAt(i);
			String str = String.valueOf(c);
			if(c == ' ') {
				continue;
			}
			arr[i] = Integer.parseInt(str);
		}
		return arr;
	}
	
	//Method that adds 9 numbers to a row. Takes in the row number and an array of nine numbers
	public void add_row(int row, int[] arr) {
		for(int i = 0; i < arr.length; i++) {
			this.grid[row][i] = arr[i];
		}
	}
	
	//Method that prompts user for input row by row and then calls the add method for each row
	public void user_input() {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the contents of the row, putting a zero in where there is a free space: ");
		int row = 0;
		while(row < 9) {
			System.out.print("Row " + (row + 1) + ": ");
			int[] arr = this.stringToNum(sc.nextLine());
			this.add_row(row, arr);
			row += 1;
			System.out.println();
		}
		sc.close();
	}
	
	//Method that adds a value to a particular cell. Three parameters: row, val, column
	public void add(int row, int col, int val) {
		this.grid[row][col] = val;
	}
	
	//Method to delete a value from a row and col, i.e, set it to zero. Two parameter: row and col
	private void delete(int row, int col) {
		this.grid[row][col] = 0;
	}
	
	//Override the string method to print out a string representation of the current state of the sudoku puzzle
	public String toString() {
		for(int i = 0; i < this.grid.length; i++) {
			System.out.print("|");
			for(int j = 0; j < this.grid[0].length; j++) {
				System.out.print(this.grid[i][j] + "|");
			}
			System.out.println();
		}
		return "";
	}
	
	//This method checks if a particular box fulfills the rules of sudoku. That is, the numbers 1 to 9 appear uniquely in the 3x3 box. 
	//This method takes in 2 parameters: The row and the col, and returns a boolean value based on if the box fulfills the sudoku rules
	private boolean check_box(int row, int col) {
		boolean isValid = true;
		if(row < 3) {
			if(col < 3) {
				isValid = check_box_one();
			}
			else if(col >= 3 && col < 6) {
				isValid = check_box_two();
			}
			else if(col >= 6 && col < 9) {
				isValid = check_box_three();
			}
		}
		
		else if(row >= 3 && row < 6) {
			if(col < 3) {
				isValid = check_box_four();
			}
			else if(col >= 3 && col < 6) {
				isValid = check_box_five();
			}
			else if(col >= 6 && col < 9) {
				isValid = check_box_six();
			}
		}
		
		else if(row >= 6 && row < 9) {
			if(col < 3) {
				isValid = check_box_seven();
			}
			else if(col >= 3 && col < 6) {
				isValid = check_box_eight();
			}
			else if(col >= 6 && col < 9) {
				isValid = check_box_nine();
			}
		}
		
		return isValid;
	}
	
	private boolean check_box_nine() {
		// TODO Auto-generated method stub
		int[] numArray = new int[10];
		int count = 0;
		
		for(int i = 6; i < 9; i++) {
			for(int j = 6; j < 9; j++) {
				numArray[this.grid[i][j]] += 1;
			}
		}
		
		int i = 1;
		while(i < 10) {
			if(numArray[i] > count) {
				count = numArray[i];
			}
			i++;
		}
		return count < 2;
	}


	private boolean check_box_eight() {
		// TODO Auto-generated method stub
		int[] numArray = new int[10];
		int count = 0;
		
		for(int i = 6; i < 9; i++) {
			for(int j = 3; j < 6; j++) {
				numArray[this.grid[i][j]] += 1;
			}
		}
		
		int i = 1;
		while(i < 10) {
			if(numArray[i] > count) {
				count = numArray[i];
			}
			i++;
		}
		return count < 2;
	}


	private boolean check_box_seven() {
		// TODO Auto-generated method stub
		int[] numArray = new int[10];
		int count = 0;
		
		for(int i = 6; i < 9; i++) {
			for(int j = 0; j < 3; j++) {
				numArray[this.grid[i][j]] += 1;
			}
		}
		
		int i = 1;
		while(i < 10) {
			if(numArray[i] > count) {
				count = numArray[i];
			}
			i++;
		}
		return count < 2;
	}


	private boolean check_box_six() {
		// TODO Auto-generated method stub
		int[] numArray = new int[10];
		int count = 0;
		
		for(int i = 3; i < 6; i++) {
			for(int j = 6; j < 9; j++) {
				numArray[this.grid[i][j]] += 1;
			}
		}
		
		int i = 1;
		while(i < 10) {
			if(numArray[i] > count) {
				count = numArray[i];
			}
			i++;
		}
		return count < 2;
	}


	private boolean check_box_five() {
		// TODO Auto-generated method stub
		int[] numArray = new int[10];
		int count = 0;
		
		for(int i = 3; i < 6; i++) {
			for(int j = 3; j < 6; j++) {
				numArray[this.grid[i][j]] += 1;
			}
		}
		
		int i = 1;
		while(i < 10) {
			if(numArray[i] > count) {
				count = numArray[i];
			}
			i++;
		}
		return count < 2;
	}


	private boolean check_box_four() {
		// TODO Auto-generated method stub
		int[] numArray = new int[10];
		int count = 0;
		
		for(int i = 3; i < 6; i++) {
			for(int j = 0; j < 3; j++) {
				numArray[this.grid[i][j]] += 1;
			}
		}
		
		int i = 1;
		while(i < 10) {
			if(numArray[i] > count) {
				count = numArray[i];
			}
			i++;
		}
		return count < 2;
	}


	private boolean check_box_three() {
		// TODO Auto-generated method stub
		int[] numArray = new int[10];
		int count = 0;
		
		for(int i = 0; i < 3; i++) {
			for(int j = 6; j < 9; j++) {
				numArray[this.grid[i][j]] += 1;
			}
		}
		
		int i = 1;
		while(i < 10) {
			if(numArray[i] > count) {
				count = numArray[i];
			}
			i++;
		}
		return count < 2;
	}


	private boolean check_box_two() {
		// TODO Auto-generated method stub
		int[] numArray = new int[10];
		int count = 0;
		
		for(int i = 0; i < 3; i++) {
			for(int j = 3; j < 6; j++) {
				numArray[this.grid[i][j]] += 1;
			}
		}
		
		int i = 1;
		while(i < 10) {
			if(numArray[i] > count) {
				count = numArray[i];
			}
			i++;
		}
		return count < 2;
	}


	private boolean check_box_one() {
		// TODO Auto-generated method stub
		int[] numArray = new int[10];
		int count = 0;
		
		for(int i = 0; i < 3; i++) {
			for(int j = 0; j < 3; j++) {
				numArray[this.grid[i][j]] += 1;
			}
		}
		
		int i = 1;
		while(i < 10) {
			if(numArray[i] > count) {
				count = numArray[i];
			}
			i++;
		}
		return count < 2;
		
	}
	
	private boolean check_row(int row) {
		int[] numArray = new int[10];
		int count = 0;
		for(int i = 0; i < 9; i++) {
			numArray[this.grid[row][i]] += 1;
		}
		
		int i = 1;
		while(i < 10) {
			if(numArray[i] > count) {
				count = numArray[i];
			}
			i++;
		}
		return count < 2;
	}
	
	private boolean check_col(int col) {
		int[] numArray = new int[10];
		int count = 0;
		for(int i = 0; i < 9; i++) {
			numArray[this.grid[i][col]] += 1;
		}
		
		int i = 1;
		while(i < 10) {
			if(numArray[i] > count) {
				count = numArray[i];
			}
			i++;
		}
		return count < 2;
	}


	//The solver method will call all the private methods made. The first implementation will use brute force to solve it
	public void solve() {
		boolean unSolvable = false;
		//Enumerate all empty cells in typewriter format
		ArrayList<Coordinate> enum_grid = new ArrayList<Coordinate>();
		for(int i = 0; i < 9; i++) {
			for(int j = 0; j < 9; j++) {
				if(this.grid[i][j] == 0) {
					enum_grid.add(new Coordinate(i,j));
				}
			}
		}
		
		int current = 0;
		while(current < enum_grid.size()) {
			Coordinate point = enum_grid.get(current);
			int row = point.getRow();
			int col = point.getCol();
			
			if(this.grid[row][col] >= 9) {
				this.delete(row, col);
				current -= 1;
				continue;
			}
			
			this.grid[row][col] += 1;
			int val = this.grid[row][col];
			
			boolean hValid = this.check_row(row);
			boolean vValid = this.check_col(col);
			boolean bValid = this.check_box(row, col);
			
			while(!hValid || !vValid || !bValid) {
				if(row == 0 && col == 0 && this.grid[row][col] >= 9) {
					unSolvable = true;
					break;
				}
				
				else if(this.grid[row][col] >= 9) {
					this.delete(row, col);
					current -= 1;
					break;
				}
				
				this.grid[row][col] += 1;
				hValid = this.check_row(row);
				vValid = this.check_col(col);
				bValid = this.check_box(row, col);
				//System.out.println(this);
				
			}
			
			if(this.grid[row][col] != 0) {
				current++;
			}
			
		}
		
		if(unSolvable) {
			return;
		}
		
		else {
			this.isSolved = true;
		}
		
		
		
	}
	
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Grid sudoku = new Grid();
		System.out.println(sudoku);
		sudoku.user_input();
		/*
		sudoku.add_row(0, new int[]{0,2,6,0,0,0,0,1,0});
		sudoku.add_row(1, new int[]{7,5,0,0,0,0,0,0,2});
		sudoku.add_row(2, new int[]{0,0,8,6,0,1,0,9,0});
		sudoku.add_row(3, new int[]{0,0,0,0,0,3,0,0,0});
		sudoku.add_row(4, new int[]{0,9,0,4,0,8,0,2,0});
		sudoku.add_row(5, new int[]{0,0,0,1,0,0,0,0,0});
		sudoku.add_row(6, new int[]{0,1,0,5,0,9,2,0,0});
		sudoku.add_row(7, new int[]{6,0,0,0,0,0,0,5,7});
		sudoku.add_row(8, new int[]{0,3,0,0,0,0,9,8,0});
		*/
		System.out.println(sudoku);
		sudoku.solve();
		System.out.println(sudoku);
		

	}

}
