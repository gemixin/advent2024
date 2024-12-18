'''
Advent of Code 2024
Day Three
https://adventofcode.com/2024/day/3
Gemma McLean
'''

from re import findall

# Read in the input file as a single string
with open('day03/input.txt') as file_object:
    mem_string = file_object.read()

# Use regex to match mul(123,123) where 123 is any 1-3 digit number
mul_regex = 'mul\\(\\d{1,3},\\d{1,3}\\)'
# Find all instances and extract to list
extracted = findall(mul_regex, mem_string)

# Extract numbers and multiply them together, summing the results
total = 0
for command in extracted:
    nums = list(map(int, findall('\\d{1,3}', command)))
    total += nums[0] * nums[1]

# Part one answer
print(total)

# Add do() and don't() to target matches in regex
new_regex = mul_regex + "|do\\(\\)|don\\'t\\(\\)"
# Find all instances and extract to list
new_extracted = findall(new_regex, mem_string)

# Loop through commands, acting accordingly
enabled = True
total = 0
for command in new_extracted:
    # If it starts with 'do'
    if command.startswith('don'):
        enabled = False
    # If it starts with 'don'
    elif command.startswith('do'):
        enabled = True
    # Otherwise (mul command)
    else:
        if enabled:
            nums = list(map(int, findall('\\d{1,3}', command)))
            total += nums[0] * nums[1]

# Part two answer
print(total)
