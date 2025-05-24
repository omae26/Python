# 24/05/2025
# 2-Dimentional lists

# number_grid = [1,2,3,4] is a normal list

# 2-D list
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
# How to access elements in the list
# the index of the row first, then the index of the column of the element you want to access
print(number_grid[2][1])

# Nested loop is a for loop inside another for loop
for row in number_grid:
    for col in row:
        print(col)  #prints all the numbers in the grid horizontally