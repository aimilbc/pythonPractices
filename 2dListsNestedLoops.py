number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
    ]

print(number_grid[0][0])    # display 1
print(number_grid[2][1])    # display 8
print(number_grid[3][0])    # display 0

for row in number_grid:     # display lists in number_grid
    print(row)

for row in number_grid:     # display single values
    for col in row:
        print(col)
