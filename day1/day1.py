'''
Advent of Code 2024
Day One
https://adventofcode.com/2024/day/1
Gemma McLean
'''

# Read in the input file as two lists of ints
with open('day1/input.txt') as file_object:
    list1, list2 = [], []
    for line in file_object:
        list1.append(int(line.split('   ')[0]))
        list2.append(int(line.split('   ')[1]))

# Sort the lists
sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

# Sum differeneces between sorted lists
total = 0
for i in range(len(sorted_list1)):
    diff = abs(sorted_list1[i] - sorted_list2[i])
    total += diff

# Part one answer
print(total)

# Sum the number in the left list * number of times it occurs in the right list
score = 0
for num in list1:
    num_list2_occs = list2.count(num)
    score += num * num_list2_occs

# Part two answer
print(score)
