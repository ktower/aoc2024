import re

MUL_RE = re.compile(r"mul\((\d+),(\d+)\)")

def tuple_to_int_and_multiply(t_list: tuple[int|str, int|str]) -> int:
    return int(t_list[0]) * int(t_list[1])

def part_1(memDump: str) -> int:
    extractedOpList = MUL_RE.findall(memDump)

    # Now we need to convert the tuples to integers and multiply them
    opTotal = 0
    for op in extractedOpList:
        opTotal += tuple_to_int_and_multiply(op)
    return opTotal


if __name__ == "__main__":
    memDumpFile = open("day3-input.txt", "r")
    memDump = memDumpFile.read()
    print(part_1(memDump))
    memDumpFile.close()