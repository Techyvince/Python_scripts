number_grid = [
    [1, 2, 3],   # This line signifies roll 0 
    [4, 5, 6],   # This line signifies roll 1 
    [7, 8, 9],   # This line signifies roll 2
    [0]          # This line signifies roll 3
]

print(number_grid[2][2]) 

for row in number_grid:
    for col in row:
        print(col)