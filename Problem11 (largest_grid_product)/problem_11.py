import numpy
def largest_grid_product(grid):
    max_rows = find_max(grid)
    max_cols = find_max(numpy.array(grid).transpose())

    matrix_grid = numpy.matrix(grid)
    diagonals_left = find_diagonals(matrix_grid)
    max_diagonals_left  = find_max(diagonals_left) 

    grid_reverse = [i[::-1] for i in grid]

    matrix_grid = numpy.matrix(grid_reverse)
    diagonals_right = find_diagonals(matrix_grid)   
    max_diagonals_right = find_max(diagonals_right)

    return  max(max_rows, max_cols, max_diagonals_left, max_diagonals_right)

def multiply_items(items):
    total = 1
    for item in items:
        total *= item
    return total

def find_diagonals(matrix_grid):
    diagonals = [list(numpy.diag(matrix_grid))]
    for i in range(1, len(matrix_grid)):
       diagonals.append(numpy.diag(matrix_grid, i))
       diagonals.append(numpy.diag(matrix_grid, -i))
    return diagonals  

def find_max(grid):
    max_mul = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if len(grid[i][j:j+4]) < 4:
                break
            items_mul = multiply_items(grid[i][j:j+4])
            if items_mul >= max_mul:
                max_mul = items_mul  
    return max_mul  


  
