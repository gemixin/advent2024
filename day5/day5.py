'''
Advent of Code 2024
Day Five
https://adventofcode.com/2024/day/5
Gemma McLean
'''

# Rules dictionary will be in the format of...
# page number: [[pages that must come before it], [pages that must come after it]]
rules = {}
# List of lists of page numbers
updates = []
# Start with section 1 of the file (rules)
section = 1

# Read in the input file in two separate sections
with open('day5/test_input.txt') as file_object:
    for line in file_object:
        # If the line is blank, switch to section 2
        if line == '\n':
            section = 2
        # Section 1 - page rules
        elif section == 1:
            # Extract the 2 numbers as ints
            rule_nums = list(map(int, line.rstrip('\n').split('|')))
            # If it's the first time seeing either number, initiate the empty lists
            for rule_num in rule_nums:
                if rule_num not in rules:
                    rules[rule_num] = [[], []]
            # Process the left hand number: append right number to its right list
            rules[rule_nums[0]][1].append(rule_nums[1])
            # Process the right hand number: append left number to its left list
            rules[rule_nums[1]][0].append(rule_nums[0])
        # Section 2 - pages to print
        elif section == 2:
            updates.append(list(map(int, line.rstrip('\n').split(','))))

total = 0
# Loop through updates
for update in updates:
    num_pages = len(update)
    correct = True
    # For each page number in the current update
    for i in range(num_pages):
        # If any of the page numbers to the left or right appear in the opposite rule list
        breach1 = any(item in update[0:i] for item in rules[update[i]][1])
        breach2 = any(item in update[i+1:num_pages] for item in rules[update[i]][0])
        if breach1 or breach2:
            # The update contains a mistake and we should break
            correct = False
            break
    # If we reach here without finding a mistake, it's a correct report
    if correct:
        # Add middle number of correct report to total
        total += update[(len(update) - 1)//2]

# Part one answer
print(total)

total = 0
# Loop through updates
for update in updates:
    num_pages = len(update)
    fixed = False
    # For each page number in the current update
    for i in range(num_pages):
        # If any of the page numbers to the left or right appear in the opposite rule list
        breach1 = any(item in update[0:i] for item in rules[update[i]][1])
        breach2 = any(item in update[i+1:num_pages] for item in rules[update[i]][0])
        if breach1 or breach2:
            # The update contains a mistake that we need to fix
            # TODO Fix the update by moving the number
            fixed = True
    # If we fixed at least one mistake
    if fixed:
        # Add middle number of fixed report to total
        total += update[(len(update) - 1)//2]

# Part two answer
print(total)
