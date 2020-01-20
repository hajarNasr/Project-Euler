from functools import reduce
import math
def lattice_paths(grid_size):
    fact_double_grid_size = reduce(lambda x, y: x*y, range(2, (grid_size*2) +1 ))  # (2 * grid_size)!
    fact_grid_size = math.pow(reduce(lambda x, y: x*y, range(2, grid_size +1)),2 ) # grid_size! * grid_size!

    return int(fact_double_grid_size / fact_grid_size)       # lattice paths = (n + m)! / n! * m!

 