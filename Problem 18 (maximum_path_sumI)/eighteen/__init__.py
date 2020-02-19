def maximum_path_sumI(triangle):
    if len(triangle) == 1:
        return triangle[0][0]
    else:    
        max_item = max_items(triangle[-1])   # => 1             # return max num between every two number in the last arr in triangle
        added_item = add_items(max_item, triangle[-2])  # => 2  # add all items in the last arr in triangle to the arr before it
        triangle = triangle[0:-2]                           # pop the last two arrays in triangle because we don't want them anymore
        triangle.append(added_item)                         # add the new array from steps one and two to be the last array in triangle 
        return maximum_path_sumI(triangle)                  # pass triangle again to the function                 # pass triangle again to the function

def max_items(arr):
    return [max(arr[i], arr[i+1]) for i in range(len(arr)-1)]   # return an array of max num between every two items in an array

def add_items(arr1, arr2):
    return [arr1[i]+ arr2[i] for i in range(len(arr1))]         # add two arrays to each other


triangle = [ [75, 0,  0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0],
             [95, 64, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0],
             [17, 47, 82, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0],
             [18, 35, 87, 10, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0],
             [20, 4, 82, 47, 65, 0, 0, 0,0, 0, 0, 0, 0, 0, 0],
             [19, 1, 23, 75, 3, 34, 0, 0,0, 0, 0, 0, 0, 0, 0],
             [88, 2, 77, 73, 7, 63, 67,0,0, 0, 0, 0, 0, 0, 0],
             [99, 65, 4, 28, 6, 16, 70, 92, 0, 0, 0, 0, 0, 0, 0],
             [41, 41, 26, 56, 83, 40, 80, 70, 33, 0, 0, 0, 0, 0, 0 ],
             [41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 0, 0, 0, 0, 0],
             [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 0, 0, 0, 0],
             [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 0, 0, 0],
             [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 0, 0],
             [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 0],
             [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
