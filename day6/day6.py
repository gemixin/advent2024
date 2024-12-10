'''
Advent of Code 2024
Day Six
https://adventofcode.com/2024/day/6
Gemma McLean
'''

# Read in the input file as a list of strings, while looking for starting_pos
with open('day6/input.txt') as file_object:
    grid = []
    for i, line in enumerate(file_object):
        # Add each line as a string to the grid
        grid.append(line.rstrip('\n'))
        # Check to see if the guard ^ is on this line
        arrow_col = line.find('^')
        # If it is, record the position
        if arrow_col != -1:
            guard_pos = (i, arrow_col)


def get_next_pos(pos, direction):
    '''
    Returns a tuple in the form (x, y) with the next potential position the guard would
    occupy based on its current position and direction.
    '''
    next_pos_x = pos[0] + direction[0]
    next_pos_y = pos[1] + direction[1]
    return (next_pos_x, next_pos_y)


def change_direction(dir_idx):
    '''
    Returns the index for the list of directions for the next direction the guard would
    face assuming it's turning 90 degrees clockwise.
    '''
    # If it's the last direction in the list, start from the beginning
    if dir_idx == len(directions) - 1:
        new_dir_idx = 0
    # Otherwise, select the next direction in the list
    else:
        new_dir_idx = dir_idx + 1
    return new_dir_idx


# Nort East South West
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# Guard starts facing North so set index for directions list to 0
guard_dir_idx = 0
# Set for visited locations including initial start position
visited = {guard_pos}


# Grid size
num_rows = len(grid)
num_cols = len(grid[0])

# Get the initial potential next position
next_pos = get_next_pos(guard_pos, directions[guard_dir_idx])
# While the guard is inside the grid
while ((next_pos[0] >= 0 and next_pos[0] < num_rows) and
       (next_pos[1] >= 0 and next_pos[1] < num_cols)):
    # Check potential new pos for obstacles
    if grid[next_pos[0]][next_pos[1]] == '#':
        guard_dir_idx = change_direction(guard_dir_idx)
    # If no obstacle, move the guard
    else:
        guard_pos = next_pos
        visited.add(next_pos)
    # Get the potential next position
    next_pos = get_next_pos(guard_pos, directions[guard_dir_idx])

# Part one answer
print(len(visited))
