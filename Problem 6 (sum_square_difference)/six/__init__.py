import math
def sum_square_difference(n):
    x =  sum(list(map(lambda x: pow(x, 2), range(1, n+1)))) # raise all numbers by 2 then add them
    y =  math.pow(sum(range(1, n+1)), 2)                    # add all numbers then raise them by 2
    return int(y - x)

    