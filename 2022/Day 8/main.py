

data = open('input.txt').read().strip()
lines = [x for x in data.split('\n')]
treesWithSight = len(lines[0]) + len(lines[len(lines) - 1]) + len(lines) * 2 - 4

# Part 1
for row in range(1, len(lines) - 1):
    for col in range(1, len(lines[row]) - 1):
        treeFound = False
        # LEFT
        for left in reversed(range(0, col)):
            if int(lines[row][left]) < int(lines[row][col]):
                if left == 0:
                    treeFound = True
            else:
                break
        if treeFound:
            treesWithSight += 1
            continue
        # RIGHT
        for right in range(col + 1, len(lines[row])):
            if int(lines[row][right]) < int(lines[row][col]):
                if right == len(lines[row]) - 1:
                    treeFound = True
            else:
                break
        if treeFound:
            treesWithSight += 1
            continue
        # UP
        for up in reversed(range(0, row)):
            if int(lines[up][col]) < int(lines[row][col]):
                if up == 0:
                    treeFound = True
            else:
                break
        if treeFound:
            treesWithSight += 1
            continue
        # DOWN
        for down in range(row + 1, len(lines)):
            if int(lines[down][col]) < int(lines[row][col]):
                if down == len(lines) - 1:
                    treeFound = True
            else:
                break
        if treeFound:
            treesWithSight += 1
            continue
print(treesWithSight)

# Part 2
maxScore = 0
for row in range(0, len(lines)):
    for col in range(0, len(lines[row])):
        leftScore = rightScore = upScore = downScore = 0
        # LEFT
        for left in reversed(range(0, col)):
            leftScore += 1
            if int(lines[row][left]) >= int(lines[row][col]):
                break
        # RIGHT
        for right in range(col + 1, len(lines[row])):
            rightScore += 1
            if int(lines[row][right]) >= int(lines[row][col]):
                break
        # UP
        for up in reversed(range(0, row)):
            upScore += 1
            if int(lines[up][col]) >= int(lines[row][col]):
                break
        # DOWN
        for down in range(row + 1, len(lines)):
            downScore += 1
            if int(lines[down][col]) >= int(lines[row][col]):
                break
        treeScore = leftScore * rightScore * upScore * downScore
        if maxScore < treeScore:
            maxScore = treeScore
print(maxScore)
