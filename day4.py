## https://adventofcode.com/2024/day/4
## Part 1: Find "XMAS" in any direction anywhere in the input file
## Part 2: Find "MAS" in the form of an X anywhere in the input file
## The input file is a word search puzzle

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

WORDSEARCH_SOURCE = []

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

def check_next_char(source: list[str], cur_x: int, cur_y: int, dir: Direction, query: str) -> bool:
    """Check the next character in the specified direction and return True if it matches the query string"""
    if dir == Direction.UP and cur_x > 0:
        return source[cur_x - 1][cur_y] == query
    elif dir == Direction.UP_RIGHT and cur_x > 0 and cur_y < len(source[cur_x - 1]) - 1:
        return source[cur_x - 1][cur_y + 1] == query
    elif dir == Direction.RIGHT and cur_y < len(source[cur_x]) - 1:
        return source[cur_x][cur_y + 1] == query
    elif dir == Direction.DOWN_RIGHT and cur_x < len(source) - 1 and cur_y < len(source[cur_x + 1]) - 1:
        return source[cur_x + 1][cur_y + 1] == query
    elif dir == Direction.DOWN and cur_x < len(source) - 1:
        return source[cur_x + 1][cur_y] == query
    elif dir == Direction.DOWN_LEFT and cur_x < len(source) - 1 and cur_y > 0:
        return source[cur_x + 1][cur_y - 1] == query
    elif dir == Direction.LEFT and cur_y > 0:
        return source[cur_x][cur_y - 1] == query
    elif dir == Direction.UP_LEFT and cur_x > 0 and cur_y > 0:
        return source[cur_x - 1][cur_y - 1] == query
    return False

if __name__ == "__main__":
    wordSearchFile = open("day4-input.txt", "r")
    WORDSEARCH_SOURCE = wordSearchFile.readlines()
    wordSearchFile.close()

    # Part 1: Find all of the "XMAS" strings in the word search
    targetString = "XMAS"
    targetFindCount = 0
    for x in range(len(WORDSEARCH_SOURCE)):
        for y in range(len(WORDSEARCH_SOURCE[x])):
            for dir in Direction:
                if find_target_string(WORDSEARCH_SOURCE, targetString, 0, x, y, dir):
                    targetFindCount += 1
    
    # Part 2: Find all instances of "MAS" in the form of an X
    targetString = "MAS"
    xTargetFindCount = 0

    for x in range(len(WORDSEARCH_SOURCE)):
        for y in range(len(WORDSEARCH_SOURCE[x])):
            xTargetFindCount = 0
    
    print(f"Part 1 - Number of 'XMAS' instances in puzzle: {targetFindCount}")