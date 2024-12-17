'''
Advent of Code 2024
Day Nine
https://adventofcode.com/2024/day/9
Gemma McLean
'''

# Read in the input file as a single string
with open('day9/input.txt') as file_object:
    input_string = file_object.read()

# Reformat the string
idx = 0
reformatted_string = []
# Dictionaries to store blocks of free space and files (used in part two)
# In the form: {index where free block starts: (number of blocks, index offset)}
free_space = {}
# In the form: {index where file block starts: number of blocks}
files = {}
# Loop through each character in the string
for i in range(len(input_string)):
    # Get the index of the start of this block of free space in output
    space_start_idx = len(reformatted_string)
    # Even numbers: files
    if i % 2 == 0:
        files[space_start_idx] = 0
        for j in range(int(input_string[i])):
            reformatted_string.append(idx)
            files[space_start_idx] += 1
        idx += 1
    # Odd numbers: free space
    else:
        # Set length of free space to 0
        free_space[space_start_idx] = 0
        free_space_count = 0
        for j in range(int(input_string[i])):
            reformatted_string.append('.')
            # Increase length of free space for every dot added
            free_space_count += 1
        free_space[space_start_idx] = (free_space_count, 0)

# Create copy for use with part one
output = reformatted_string.copy()

# Pointer for start of list
j = 0
# Loop through each character in the list backwards, from the end
for i in range(len(output)-1, -1, -1):
    # Don't overlap i and j
    if i - 1 <= j:
        break
    # Ignore free space
    if output[i] != '.':
        # Increment j until it reaches the next free block
        while output[j] != '.':
            j += 1
        # Insert the number at i in to position j and '.' at position i
        output[j] = output[i]
        output[i] = '.'


def calculate_checksum(output_list):
    ''' Calculate checksum by multiplying index by num and summing. '''
    checksum = 0
    for i, num in enumerate(output_list):
        # Skip free space
        if (num != '.'):
            checksum += i * num
    return checksum


# Part one answer
print(calculate_checksum(output))

# Create fresh copy for use with part two
output = reformatted_string.copy()

for file_key in reversed(files):
    # Number of blocks for current file
    num_blocks = files[file_key]
    # Start index for current file
    start_idx = file_key
    # End index for current file (start+num_blocks)
    end_idx = start_idx + num_blocks
    # Loop through available free space
    for free_key in free_space:
        # Only look at free blocks on the left of current file
        if free_key >= file_key:
            break
        # If we find a block of free space large enough
        if free_space[free_key][0] >= num_blocks:
            # Replace the free space with the file
            offset = free_space[free_key][1]
            output[free_key + offset:free_key + offset +
                   num_blocks] = output[start_idx:end_idx]
            # Replace the file with free space
            output[start_idx:end_idx] = ['.' for _ in range(start_idx, end_idx)]
            # Calculate number of free blocks leftover
            remaining_blocks = free_space[free_key][0] - num_blocks
            # If they've all been used, delete from dictionary
            if remaining_blocks == 0:
                del free_space[free_key]
            # If some blocks are left
            else:
                # Increase new offset for where block starts
                new_offset = free_space[free_key][1] + num_blocks
                # Update dictionary
                free_space[free_key] = (remaining_blocks, new_offset)
            break

# Part two answer
print(calculate_checksum(output))
