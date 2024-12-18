'''
Advent of Code 2024
Day Seven
https://adventofcode.com/2024/day/7
Gemma McLean
'''

# Read in the input file as a list of tuples in the form (target_num, [operands])
with open('day07/input.txt') as file_object:
    calibrations = []
    for line in file_object:
        # Get the target number as an int
        num = int(line.split(':')[0])
        # Get the operands as a list of ints
        operands = list(map(int, line.split(':')[1].split(' ')[1:]))
        # Add as a tuple to the list
        calibrations.append((num, operands))


def dfs_calibration(target, operands, include_concat=False):
    '''
    Perform a depth-first search on the calibrations.
    Returns True if the operands can form the target and False if not.
    Set include_concat to True to include concatenation as a possible operator.
    Each stack entry is (current_result, index)
    Index = index of the next operand we need to consider
    '''
    # If there are no operands, return False
    if not operands:
        return False

    # Initialise the stack for DFS with the first operand as the initial result
    stack = [(operands[0], 1)]

    # While the stack isn't empty
    while stack:
        # Pop the top of the stack
        current_result, index = stack.pop()

        # Prune paths where the current result exceeds the target
        if current_result > target:
            continue

        # If all operands have been processed, check final total
        if index == len(operands):
            if current_result == target:
                return True
            continue

        # Get the next operand
        next_operand = operands[index]

        # Push the next states to the stack
        stack.append((current_result + next_operand, index + 1))
        stack.append((current_result * next_operand, index + 1))
        # If the || concat operator is in use (part two)
        if include_concat:
            concatenated = str(current_result) + str(next_operand)
            stack.append((int(concatenated), index + 1))

    # If the stack is empty and the target hasn't been reached
    return False


total = 0
# Loop through calibrations
for cal in calibrations:
    result = dfs_calibration(cal[0], cal[1])
    if result:
        total += cal[0]

# Part one answer
print(total)

total = 0
# Loop through calibrations
for cal in calibrations:
    result = dfs_calibration(cal[0], cal[1], include_concat=True)
    if result:
        total += cal[0]

# Part two answer
print(total)
