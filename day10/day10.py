'''
Advent of Code 2024
Day Ten
https://adventofcode.com/2024/day/10
Gemma McLean
'''

import numpy as np

# Read in the input file as a list of list of ints
with open('day10/input.txt') as file_object:
    # Empty lists for storing the map and trailhead positions
    top_map = []
    trailhead_positions = []
    for i, line in enumerate(file_object):
        # Each row is a new list
        row_list = []
        # Append each number as an int
        for j, char in enumerate(line.rstrip('\n')):
            row_list.append(int(char))
            # If we find a 0, make a note of its position within the map
            if char == '0':
                trailhead_positions.append(np.array([i, j]))
        top_map.append(row_list)


def dfs_climb(top_map, trailhead_pos, ratings=False):
    '''
    Perform a depth-first search on the topological map.
    Starts from a trailhead position (0) and attempts to find all possible paths
    to the peaks (9s) by following a path that increases by exactly 1 at eash step.
    Returns the number of unique peaks that can be reached from trailhead position.
    '''
    # Initialise the stack for DFS with the trailhead position
    stack = [trailhead_pos]
    # Empty set for storing peak positions
    peaks = set()
    # Empty list for part two peak positions
    ratings_peaks = []
    # Nort East South West
    directions = [np.array([-1, 0]), np.array([0, 1]),
                  np.array([1, 0]), np.array([0, -1])]
    # Map size
    num_rows = len(top_map)
    num_cols = len(top_map[0])

    # While the stack isn't empty
    while stack:
        # Pop the top of the stack
        current_pos = stack.pop()

        # If we've reached a peak (9), add it to the list/set
        if top_map[current_pos[0]][current_pos[1]] == 9:
            if ratings:
                ratings_peaks.append((current_pos[0], current_pos[1]))
            else:
                peaks.add((current_pos[0], current_pos[1]))

        # Explore adjacent locations
        for direction in directions:
            next_pos = current_pos + direction
            # If it's within the grid
            if ((next_pos[0] >= 0 and next_pos[0] < num_rows) and
                    (next_pos[1] >= 0 and next_pos[1] < num_cols)):
                # If the location is one step higher
                next_val = top_map[next_pos[0]][next_pos[1]]
                current_val = top_map[current_pos[0]][current_pos[1]]
                if (next_val == current_val + 1):
                    # Push next position to stack
                    stack.append(next_pos)

    # If the stack is empty we've finished searching
    # Return the number of unique paths
    if ratings:
        return len(ratings_peaks)
    # Return the number of unique peaks reached
    else:
        return len(peaks)


# Run DFS for each trailhead position
total = 0
for pos in trailhead_positions:
    total += dfs_climb(top_map, pos)

# Part one answer
print(total)

# Run DFS for each trailhead position with ratings set to true
total = 0
for pos in trailhead_positions:
    total += dfs_climb(top_map, pos, True)

# Part two answer
print(total)
