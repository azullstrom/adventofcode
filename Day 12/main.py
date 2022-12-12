# Kudos to jonathanpaulson. Learned alot.
from collections import deque
data = open("input.txt").read().strip()
lines = [x for x in data.split('\n')]

GRID = []
for line in lines:
    GRID.append(line)
ROW = len(GRID)
COL = len(GRID[0])
# Adding 2D array with size of GRID
ELEMENTS = [[0 for x in range(COL)] for y in range(ROW)]
for row in range(ROW):
    for col in range(COL):
        if GRID[row][col] == 'S':
            ELEMENTS[row][col] = 1
        elif GRID[row][col] == 'E':
            ELEMENTS[row][col] = 26
        else:
            # Checking ascii value and takes away 'a' value for decimal representation. 'a' = 97 - 97 + 1, b = 98 - 97 + 1...
            ELEMENTS[row][col] = ord(GRID[row][col]) - ord('a') + 1

def breadth_first_search():
    Q = deque()
    for row in range(ROW):
        for col in range(COL):
            if GRID[row][col] == 'S':
                # Start node
                Q.append(((row, col), 0))
    S = set()
    while Q:
        (row, col), depth = Q.popleft()
        if (row, col) in S:
            continue

        S.add((row, col))

        if GRID[row][col] == 'E':
            return depth

        for dir_row, dir_col in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            next_row = row + dir_row
            next_col = col + dir_col
            if 0 <= next_row < ROW and 0 <= next_col < COL and ELEMENTS[next_row][next_col] <= 1 + ELEMENTS[row][col]:
                Q.append(((next_row, next_col), depth + 1))

print("part one: ", breadth_first_search())

