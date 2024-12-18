'''
Advent of Code 2024
Day Two
https://adventofcode.com/2024/day/2
Gemma McLean
'''

# Read in the input file as a list of lists of ints
with open('day02/input.txt') as file_object:
    reports = [list(map(int, line.split(' '))) for line in file_object]


def check_report(report):
    ''' Returns True if report is safe and False if unsafe. '''
    # Values in descending order within 1-3 of each other
    if all(report[i] > report[i+1] and abs(report[i] - report[i+1]) in range(1, 4)
           for i in range(len(report)-1)):
        return True
    # Values in ascending order within 1-3 of each other
    elif all(report[i] < report[i+1] and abs(report[i] - report[i+1]) in range(1, 4)
             for i in range(len(report)-1)):
        return True
    else:
        return False


def check_report_using_sets(report):
    ''' Returns True if report is safe and False if unsafe. This approach uses sets.'''
    # Allowed difference values for an ascending list
    pos_diffs = {1, 2, 3}
    # Allowed difference values for an descending list
    neg_diffs = {-1, -2, -3}
    # Get difference between num and previous number and add it to both sets
    for i in range(1, len(report)):
        pos_diffs.add(report[i] - report[i-1])
        neg_diffs.add(report[i] - report[i-1])
    if len(pos_diffs) == 3 or len(neg_diffs) == 3:
        return True
    else:
        return False


# Check each report
safe_reports = 0
for report in reports:
    if check_report_using_sets(report):
        safe_reports += 1

# Part one answer
print(safe_reports)

# Check each report again but allow for 1 deletion
safe_reports = 0
for report in reports:
    # Check full report
    if check_report_using_sets(report):
        safe_reports += 1
    else:
        # Check report without current value
        for i in range(len(report)):
            new_report = report.copy()
            new_report.pop(i)
            # If it's safe, stop checking
            if check_report_using_sets(new_report):
                safe_reports += 1
                break

# Part two answer
print(safe_reports)
