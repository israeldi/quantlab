# A Backtracking program in Python to solve Sudoku problem
  
  
# Prints entire grid, with two dimensional array as input
def print_grid(arr): 
    '''
    Your Code Here
    
    '''

       
# Function to Find the entry in the Grid that is still not used 
# Searches the grid to find an entry that is still unassigned. If 
# found, the reference parameters row, col will be set the location 
# that is unassigned, and true is returned. If no unassigned entries 
# remain, false is returned. 
# 'l' is a list  variable that has been passed from the solve_sudoku function 
# to keep track of incrementation of Rows and Columns 
def find_empty_location(arr, l): 
    # Check for the first zero entry and assign the corresponding
    # row, column indices to l, i.e. l[0] = firsZerorow, l[1] = firstZerocol.
    
    '''
    Your Code Here
    
    '''

    
    # Return False if there are no non-zero entries
    return False
  
# Returns a boolean which indicates whether any assigned entry 
# in the specified row matches the given number. 
def used_in_row(arr, row, num): 
    for i in range(9): 
        '''
        Your Code Here
        
        '''
    return False
  
# Returns a boolean which indicates whether any assigned entry 
# in the specified column matches the given number. 
def used_in_col(arr,col,num): 
    for i in range(9): 
        '''
        Your Code Here
        
        '''
    return False
  
# Returns a boolean which indicates whether any assigned entry 
# within the specified 3x3 box matches the given number 
def used_in_box(arr,row,col,num): 
    for i in range(3): 
        for j in range(3): 
            '''
            Your Code Here
            
            '''
    return False
  
# Checks whether it will be legal to assign num to the given row,col 
#  Returns a boolean which indicates whether it will be legal to assign 
#  num to the given row,col location. 
def check_location_is_safe(arr,row,col,num): 
      
    # Check if 'num' is not already placed in current row, 
    # current column and current 3x3 box 
    '''
    Your Code Here
            
    '''
  
# Takes a partially filled-in grid and attempts to assign values to 
# all unassigned locations in such a way to meet the requirements 
# for Sudoku solution (non-duplication across rows, columns, and boxes) 
def solve_sudoku(arr): 
      
    # 'l' is a list variable that keeps the record of row and col in find_empty_location Function     
    l=[0,0] 
      
    # If there is no unassigned location, we are done     
    if(not find_empty_location(arr,l)): 
        return True
      
    # Assigning list values to row and col to first zero-entry  
    row = l[0]; col = l[1] 
      
    # consider digits 1 to 9 
    for num in range(1,10): 
        
        # Use Recursion to find a solution
        '''
        Your Code Here
                
        '''
        
              
    # this triggers backtracking         
    return False 
  
# Driver main function to test above functions -------------------------------
if __name__=="__main__": 
      
    # assigning values to the grid 
    
    grid=[[0,0,0, 0,0,0, 0,0,0], 
          [0,0,0, 0,0,0, 0,0,0], 
          [0,0,0, 0,0,0, 0,0,0], 
          
          [0,0,0, 0,0,0, 0,0,0], 
          [0,0,0, 0,0,0, 0,0,0], 
          [0,0,0, 0,0,0, 0,0,0],
          
          [0,0,0, 0,0,0, 0,0,0], 
          [0,0,0, 0,0,0, 0,0,0], 
          [0,0,0, 0,0,0, 0,0,0]] 
       
    # if sucess print the grid 
    if(solve_sudoku(grid)): 
        print_grid(grid)
                
    else: 
        print("No solution exists")
        
        