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
with open('day5/input.txt') as file_object:
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


def check_update(update):
    '''
    Returns True if the given update contains no errors.
    Returns False if even one error is found.
    An error is when a page number violates the rules by appearing before or
    after a number it shouldn't do.
    '''
    num_pages = len(update)
    # For each page number in the current update
    for i in range(num_pages):
        # If any of the page numbers to the left or right appear in the opposite rule list
        error1 = any(item in update[0:i] for item in rules[update[i]][1])
        error2 = any(item in update[i+1:num_pages] for item in rules[update[i]][0])
        if error1 or error2:
            # The update contains an error so immediately return False
            return False
    # If this code is reached, there are no errors so return True
    return True


total = 0
# Loop through updates
for update in updates:
    # If update is correct
    if check_update(update):
        # Add middle number of correct update to total
        total += update[(len(update) - 1) // 2]

# Part one answer
print(total)


def recursive_sort(page, sorted_update, processed, relevant_rules):
    ''' Recursively sort the pages of an update according to the rules. '''
    # Skip already processed pages
    if page in processed:
        return  # Skip if already processed
    # Track which pages have been processed
    processed.add(page)
    # Ensure all dependencies are placed before the current page
    for before_page in relevant_rules[page][0]:
        # Only consider relevant dependencies
        if before_page in relevant_rules:
            recursive_sort(before_page, sorted_update, processed, relevant_rules)
    # Add the current page if it's not already in the sorted list
    if page not in sorted_update:
        sorted_update.append(page)


total = 0
# Loop through updates
for update in updates:
    # If update contains at least one error
    if not check_update(update):
        # Empty list for newly sorted update
        sorted_update = []
        # Empty set to track which numbers have been processed
        processed = set()
        # Extract relevant rules for pages in this update
        relevant_rules = {page: rules[page] for page in update}
        # Reorder the incorrectly sorted update
        for page in update:
            recursive_sort(page, sorted_update, processed, relevant_rules)
        # Add the middle number of the sorted update to the total
        total += sorted_update[(len(sorted_update) - 1) // 2]

# Part two answer
print(total)
