def spiral_diagonals(n):
    result = 1
    for i in range(3, n+1, 2):
        result += 4 * (i**2) - 6*i +6     # stolen equation, tbh
    return result    