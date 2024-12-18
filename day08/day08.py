'''
Advent of Code 2024
Day Eight
https://adventofcode.com/2024/day/8
Gemma McLean
'''

import numpy as np

# Read in the input file as a dictionary of antenna positions
with open('day08/input.txt') as file_object:
    # Empty dictionary for antennas
    antennas = {}
    for i, line in enumerate(file_object):
        for j, char in enumerate(line.rstrip('\n')):
            # If it's an antenna (frequency = char)
            if char != '.':
                # If the frequency is not already in the dictionary
                if char not in antennas.keys():
                    # Create the key and create a list with first position
                    # Use Numpy array for position for easy element-wise operations
                    antennas[char] = [np.array([i, j])]
                else:
                    # Add the position for the current frequency
                    antennas[char].append(np.array([i, j]))

# Store grid size for checking later
grid_size = np.array([i+1, j+1])

# An empty set for antinode positions
antinodes = set()
# Loop through the keys
for freq in antennas.keys():
    # Get the list of antenna positions for that frequency
    positions = antennas[freq]
    # Create a list of all pairs of antenna positions in the form ((x,y), (x,y))
    pairs = [(a, b) for i, a in enumerate(positions) for b in positions[i + 1:]]
    # For each pair of positions
    for pair in pairs:
        # Get vector difference
        diff = pair[1] - pair[0]
        # Subtract from pair[0] and add to pair[1] to get antinode positions
        anti_pos1 = pair[0] - diff
        anti_pos2 = pair[1] + diff
        # Don't include any that are outside grid shape
        # Add antinodes to a set (as tuples)
        if (anti_pos1 < grid_size).all() and (anti_pos1 >= 0).all():
            antinodes.add(tuple(anti_pos1))
        if (anti_pos2 < grid_size).all() and (anti_pos2 >= 0).all():
            antinodes.add(tuple(anti_pos2))

# Part one answer
print(len(antinodes))

# An empty set for antinode positions
antinodes = set()
# Loop through the keys
for freq in antennas.keys():
    # Get the list of antenna positions for that frequency
    positions = antennas[freq]
    # Add all antennas for this frequency to the antinodes set
    antinodes.update([tuple(pos) for pos in positions])
    # Create a list of all pairs of antenna positions in the form ((x,y), (x,y))
    pairs = [(a, b) for i, a in enumerate(positions) for b in positions[i + 1:]]
    # For each pair of positions
    for pair in pairs:
        # Get vector difference
        diff = pair[1] - pair[0]
        # Subtract from pair[0] to get initial first antinode position
        anti_pos1 = pair[0] - diff
        # While it's inside the grid, keep adding antinodes at the same distance
        while (anti_pos1 < grid_size).all() and (anti_pos1 >= 0).all():
            # Subtract from pair[0] and add to pair[1] to get antinode positions
            antinodes.add(tuple(anti_pos1))
            anti_pos1 = anti_pos1 - diff
        # Add to pair[1] to get initial second antinode position
        anti_pos2 = pair[1] + diff
        # While it's inside the grid, keep adding antinodes at the same distance
        while (anti_pos2 < grid_size).all() and (anti_pos2 >= 0).all():
            antinodes.add(tuple(anti_pos2))
            anti_pos2 = anti_pos2 + diff

# Part two answer
print(len(antinodes))
