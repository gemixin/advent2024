'''
Advent of Code 2024
Day Four
https://adventofcode.com/2024/day/4
Gemma McLean
'''

# Read in the input file as a list of strings
with open('day04/input.txt') as file_object:
    grid = [line.rstrip('\n') for line in file_object]

# Set some variables
num_rows = len(grid)
num_cols = len(grid[0])
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
letters = 'XMAS'


def check_direction(i, j, direction):
    ''' Returns True if XMAS is spelled in the specified direction, False if not. '''
    # Calculate the grid location for 3 squares in the specified direction
    max_square = (i + 3 * (direction[0]), j + 3 * (direction[1]))
    # If the location exists in the grid
    if (max_square[0] < num_rows and max_square[0] >= 0
            and max_square[1] < num_cols and max_square[1] >= 0):
        # Check each square in the specified direction, one step at a time
        for k in range(1, 4):
            new_i = i + k * (direction[0])
            new_j = j + k * (direction[1])
            # If the letter does not match the pattern, immediately return False
            if not grid[new_i][new_j] == letters[k]:
                return False
        # If it reaches the end of the loop, all 4 squares spell XMAS
        return True
    # If the location does not exist in the grid
    # (i.e. a 4 letter word can't exist in direction starting from i,j)
    return False


total = 0
# Loop through grid
for i in range(num_rows):
    for j in range(num_cols):
        # Check each X
        if grid[i][j] == 'X':
            # Check each possible direction
            for direction in directions:
                # If it spells XMAS, increase the total
                if check_direction(i, j, direction):
                    total += 1

# Part one answer
print(total)

# Starting from top left going clockwise
diag_positions = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
allowed_patterns = ['SSMM', 'MMSS', 'MSSM', 'SMMS']

total = 0
# Loop through the grid ignoring the first and last row and column
for i in range(1, num_rows-1):
    for j in range(1, num_cols-1):
        # Check each A
        if grid[i][j] == 'A':
            pattern = ''
            # Get the 4 diagonals
            for pos in diag_positions:
                new_i = i + pos[0]
                new_j = j + pos[1]
                pattern += grid[new_i][new_j]
            # If the patterns match, increase the total
            if pattern in allowed_patterns:
                total += 1

# Part two answer
print(total)
