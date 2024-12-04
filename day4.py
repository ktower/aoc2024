## https://adventofcode.com/2024/day/4
## Find "XMAS" anywhere in the input file
from enum import Enum

class Direction(Enum):
    UP = 1
    UP_RIGHT = 2
    RIGHT = 3
    DOWN_RIGHT = 4
    DOWN = 5
    DOWN_LEFT = 6
    LEFT = 7
    UP_LEFT = 8

TARGET_STRING = "XMAS"
WORDSEARCH_SOURCE = []
TARGET_FIND_COUNT = 0

def find_target_string(source: list[str], target: str, target_index: int, cur_x: int, cur_y: int, dir: Direction) -> bool:
    # So far so good, the current character matches the target character, keep looking in the same direction
    if source[cur_x][cur_y] == target[target_index]:
        # Recursive base-case: If we found the last character in the target string then we have a match
        if target_index == len(target) - 1:
            return True
        elif dir == Direction.UP and cur_x > 0:
            return find_target_string(source, target, target_index + 1, cur_x - 1, cur_y, dir)
        elif dir == Direction.UP_RIGHT and cur_x > 0 and cur_y < len(source[cur_x - 1]) - 1:
            return find_target_string(source, target, target_index + 1, cur_x - 1, cur_y + 1, dir)
        elif dir == Direction.RIGHT and cur_y < len(source[cur_x]) - 1:
            return find_target_string(source, target, target_index + 1, cur_x, cur_y + 1, dir)
        elif dir == Direction.DOWN_RIGHT and cur_x < len(source) - 1 and cur_y < len(source[cur_x + 1]) - 1:
            return find_target_string(source, target, target_index + 1, cur_x + 1, cur_y + 1, dir)
        elif dir == Direction.DOWN and cur_x < len(source) - 1:
            return find_target_string(source, target, target_index + 1, cur_x + 1, cur_y, dir)
        elif dir == Direction.DOWN_LEFT and cur_x < len(source) - 1 and cur_y > 0:
            return find_target_string(source, target, target_index + 1, cur_x + 1, cur_y - 1, dir)
        elif dir == Direction.LEFT and cur_y > 0:
            return find_target_string(source, target, target_index + 1, cur_x, cur_y - 1, dir)
        elif dir == Direction.UP_LEFT and cur_x > 0 and cur_y > 0:
            return find_target_string(source, target, target_index + 1, cur_x - 1, cur_y - 1, dir)

    # If we get here then we don't have a match at this location in any direction
    return False


if __name__ == "__main__":
    wordSearchFile = open("day4-input.txt", "r")
    WORDSEARCH_SOURCE = wordSearchFile.readlines()
    wordSearchFile.close()
    #print(f"Read in word search file with {len(WORDSEARCH_SOURCE)} lines")
    for x in range(len(WORDSEARCH_SOURCE)):
        for y in range(len(WORDSEARCH_SOURCE[x])):
            for dir in Direction:
                if find_target_string(WORDSEARCH_SOURCE, TARGET_STRING, 0, x, y, dir):
                    TARGET_FIND_COUNT += 1
    
    print(TARGET_FIND_COUNT)