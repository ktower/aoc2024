# Take as an input a file with 2 or more numbers per line representing reports.
# For each line if the numbers are all either increasing or decreasing, and
# the difference between each element is between a preset minimum and maximum
# then the line is considered "safe."
# 
# As a final output print a count of the number of safe lines.

MIN_SAFE = 1
MAX_SAFE = 3

def list_to_int(list):
    return [int(i) for i in list]

def is_sorted(lst):
    if all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)):
        return True  # List is sorted in increasing order
    if all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1)):
        return True  # List is sorted in decreasing order
    return False  # List is not sorted

def is_safe(lst):
    safe = True
    for i in range(len(lst) - 1):
        if abs(lst[i + 1] - lst[i]) < MIN_SAFE or abs(lst[i + 1] - lst[i]) > MAX_SAFE:
            safe = False
            break
    return safe

listFile = open("day2-input.txt", "r")

safeCount = 0

for line in listFile:
    reportList = list_to_int(line.split())

    if is_sorted(reportList) and is_safe(reportList):
        safeCount += 1
    else:
        # Remove one item from the list and check again; we can accept one "out of bound" value
        for i in range(len(reportList)):
            shortList = reportList.copy()
            shortList.pop(i)
            if is_sorted(shortList) and is_safe(shortList):
                safeCount += 1
                break

print(f"Number of safe reports: {safeCount}")