# Take as an input a file with 2 or more numbers per line representing reports.
# For each line if the numbers are all either increasing or decreasing, and
# the difference between each element is between a preset minimum and maximum
# then the line is considered "safe."
# 
# As a final output print a count of the number of safe lines.

MIN_SAFE = 1
MAX_SAFE = 3

def is_sorted(lst):
    if all(int(lst[i]) <= int(lst[i + 1]) for i in range(len(lst) - 1)):
        return True  # List is sorted in increasing order
    if all(int(lst[i]) >= int(lst[i + 1]) for i in range(len(lst) - 1)):
        return True  # List is sorted in decreasing order
    return False  # List is not sorted

listFile = open("day2-input.txt", "r")

safeCount = 0

for line in listFile:
    reportList = line.split()

    if is_sorted(reportList):
        safe = True
        for i in range(len(reportList) - 1):
            if abs(int(reportList[i + 1]) - int(reportList[i])) < MIN_SAFE or abs(int(reportList[i + 1]) - int(reportList[i])) > MAX_SAFE:
                safe = False
                break
        if safe:
            safeCount += 1

print(f"Number of safe reports: {safeCount}")