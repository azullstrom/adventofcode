

data = open('input.txt').read().strip()
lines = [x for x in data.split('\n')]
treesWithSight = len(lines[0]) + len(lines[len(lines) - 1]) + len(lines) * 2 - 4

for row in range(1, len(lines) - 1):
    for col in range(1, len(lines[row]) - 1):
        tree = 0
        #LEFT
        for left in reversed(range(0, col)):
            if int(lines[row][left]) < int(lines[row][col]):
                if left == 0:
                    tree += 1
            else:
                break
        if tree == 1:
            treesWithSight += 1
            continue
        #RIGHT
        for right in range(col + 1, len(lines[row])):
            if int(lines[row][right]) < int(lines[row][col]):
                if right == len(lines[row]) - 1:
                    tree += 1
            else:
                break
        if tree == 1:
            treesWithSight += 1
            continue
        #UP
        for up in reversed(range(0, row)):
            if int(lines[up][col]) < int(lines[row][col]):
                if up == 0:
                    tree += 1
            else:
                break
        if tree == 1:
            treesWithSight += 1
            continue
        #DOWN
        for down in range(row + 1, len(lines)):
            if int(lines[down][col]) < int(lines[row][col]):
                if down == len(lines) - 1:
                    tree += 1
            else:
                break
        if tree == 1:
            treesWithSight += 1
            continue
print(treesWithSight)