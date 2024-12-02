listfile = open("day1-input.txt", "r")

list1 = []
list2 = []

for line in listfile:
    if line.strip():  # Verify the line isn't empty
        numbers = line.split()
        if len(numbers) == 2:
            list1.append(int(numbers[0]))
            list2.append(int(numbers[1]))

listfile.close()

list1.sort()
list2.sort()

if len(list1) != len(list2):
    print("Lists are not the same length")
    exit()

listdiff = 0

for i in range(len(list1)):
    if list1[i] > list2[i]:
        listdiff += list1[i] - list2[i]
    else:
        listdiff += list2[i] - list1[i]

print("The sum of the differences between the two lists is", listdiff)
