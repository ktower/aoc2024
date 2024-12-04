import re

## Some logic roughly based on:
## https://github.com/danielenricocahall/AdventOfCode2024/blob/main/day_3/solution.py

MUL_RE = re.compile(r"mul\((\d+),(\d+)\)")
DO_RE = re.compile(r"do\(\)")
DONT_RE = re.compile(r"don't\(\)")

def tuple_to_int_and_multiply(t_list: tuple[int|str, int|str]) -> int:
    return int(t_list[0]) * int(t_list[1])

def part_1(memDump: str) -> int:
    extractedOpList = MUL_RE.findall(memDump)

    # Now we need to convert the tuples to integers and multiply them
    opTotal = 0
    for op in extractedOpList:
        opTotal += tuple_to_int_and_multiply(op)
    return opTotal

def part_2(memDump: str) -> int:
    enabled = True  # Start with the mul operation enabled
    opTotal = 0
    cur_string = ""

    for char in memDump:
        cur_string += char
        if DO_RE.findall(cur_string):
            enabled = True
            cur_string = ""
        elif DONT_RE.findall(cur_string):
            enabled = False
            cur_string = ""
        elif opMatch := MUL_RE.findall(cur_string):
            if enabled:
                for op in opMatch:
                    opTotal += tuple_to_int_and_multiply(op)
            cur_string = ""
    return opTotal


if __name__ == "__main__":
    memDumpFile = open("day3-input.txt", "r")
    memDump = memDumpFile.read()
    print(part_1(memDump))
    print(part_2(memDump))
    memDumpFile.close()