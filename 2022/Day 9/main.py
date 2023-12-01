from enum import Enum


class DIRECTION(Enum):
    NO_MOVE = 0
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4


def distancedFromHead(xHead, yHead, xTail, yTail):
    distanced = DIRECTION.NO_MOVE

    if xHead - xTail == 2:
        distanced = DIRECTION.RIGHT
    elif xTail - xHead == 2:
        distanced = DIRECTION.LEFT
    elif yHead - yTail == 2:
        distanced = DIRECTION.UP
    elif yTail - yHead == 2:
        distanced = DIRECTION.DOWN
    return distanced


def moveTail(number, direction):
    if direction == DIRECTION.LEFT:
        return number - 1
    elif direction == DIRECTION.RIGHT:
        return number + 1
    elif direction == DIRECTION.UP:
        return number + 1
    elif direction == DIRECTION.DOWN:
        return number - 1


def printRope(tailPosX, tailPosY):
    for i in range(len(tailPosX)):
        print(tailPosX[i], tailPosY[i], '|', end='')
    print('')


if __name__ == '__main__':
    data = open("test.txt").read()
    lines = [x for x in data.split('\n')]
    headPosX = headPosY = tailPosX = tailPosY = 0
    xVisited = {'x0 y0'}
    yVisited = {'x0 y0'}
    # Part 1
    for line in lines:
        direction_line, step = line.strip().split()

        # HEAD TURN
        if direction_line == 'L':
            for left in range(int(step)):
                headPosX -= 1
                xVisited.add("x" + str(headPosX) + " y" + str(headPosY))
                direction = distancedFromHead(headPosX, headPosY, tailPosX, tailPosY)
                if direction != DIRECTION.NO_MOVE:
                    tailPosX = moveTail(tailPosX, direction)
                    tailPosY = headPosY
                    yVisited.add("x" + str(tailPosX) + " y" + str(tailPosY))
        elif direction_line == 'R':
            for right in range(int(step)):
                headPosX += 1
                xVisited.add("x" + str(headPosX) + " y" + str(headPosY))
                direction = distancedFromHead(headPosX, headPosY, tailPosX, tailPosY)
                if direction != DIRECTION.NO_MOVE:
                    tailPosX = moveTail(tailPosX, direction)
                    tailPosY = headPosY
                    yVisited.add("x" + str(tailPosX) + " y" + str(tailPosY))
        elif direction_line == 'U':
            for up in range(int(step)):
                headPosY += 1
                xVisited.add("x" + str(headPosX) + " y" + str(headPosY))
                direction = distancedFromHead(headPosX, headPosY, tailPosX, tailPosY)
                if direction != DIRECTION.NO_MOVE:
                    tailPosY = moveTail(tailPosY, direction)
                    tailPosX = headPosX
                    yVisited.add("x" + str(tailPosX) + " y" + str(tailPosY))
        elif direction_line == 'D':
            for down in range(int(step)):
                headPosY -= 1
                xVisited.add("x" + str(headPosX) + " y" + str(headPosY))
                direction = distancedFromHead(headPosX, headPosY, tailPosX, tailPosY)
                if direction != DIRECTION.NO_MOVE:
                    tailPosY = moveTail(tailPosY, direction)
                    tailPosX = headPosX
                    yVisited.add("x" + str(tailPosX) + " y" + str(tailPosY))
    # print(xVisited)
    print("Part one:", len(yVisited))

    # Part 2 NOT DONE
    headPosX = headPosY = 0
    tailPosX = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    tailPosY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    xVisited = {'x0 y0'}
    yVisited = {'x0 y0'}

    for line in lines:
        direction_line, step = line.strip().split()
        #print(direction_line)
        if direction_line == 'L':
            for left in range(int(step)):
                print("l", end='')
                printRope(tailPosX, tailPosY)
                headPosX -= 1
                tailPosX[0] = headPosX
                xVisited.add("x" + str(headPosX) + " y" + str(headPosY))
                direction = distancedFromHead(headPosX, headPosY, tailPosX[1], tailPosY[1])
                for i in range(1, len(tailPosX)):
                    if direction != DIRECTION.NO_MOVE:
                        tailPosX[i] = moveTail(tailPosX[i], direction)
                        tailPosY[i] = tailPosY[i - 1]
                        if i < len(tailPosX) - 1:
                            direction = distancedFromHead(tailPosX[i], tailPosY[i], tailPosX[i+1], tailPosY[i+1])
                        else:
                            yVisited.add("x" + str(tailPosX[i]) + " y" + str(tailPosY[i]))
        elif direction_line == 'R':
            for right in range(int(step)):
                print("r", end='')
                printRope(tailPosX, tailPosY)
                headPosX += 1
                tailPosX[0] = headPosX
                xVisited.add("x" + str(headPosX) + " y" + str(headPosY))
                direction = distancedFromHead(headPosX, headPosY, tailPosX[1], tailPosY[1])
                for i in range(1, len(tailPosX)):
                    if direction != DIRECTION.NO_MOVE:
                        tailPosX[i] = moveTail(tailPosX[i], direction)
                        tailPosY[i] = tailPosY[i - 1]
                        if i < len(tailPosX) - 1:
                            direction = distancedFromHead(tailPosX[i], tailPosY[i], tailPosX[i + 1], tailPosY[i + 1])
                        else:
                            yVisited.add("x" + str(tailPosX[i]) + " y" + str(tailPosY[i]))
        elif direction_line == 'U':
            for up in range(int(step)):
                print("u", end='')
                printRope(tailPosX, tailPosY)
                headPosY += 1
                tailPosY[0] = headPosY
                xVisited.add("x" + str(headPosX) + " y" + str(headPosY))
                direction = distancedFromHead(headPosX, headPosY, tailPosX[1], tailPosY[1])
                for i in range(1, len(tailPosX)):
                    if direction != DIRECTION.NO_MOVE:
                        tailPosY[i] = moveTail(tailPosY[i], direction)
                        tailPosX[i] = tailPosX[i - 1]
                        if i < len(tailPosX) - 1:
                            direction = distancedFromHead(tailPosX[i], tailPosY[i], tailPosX[i + 1], tailPosY[i + 1])
                        else:
                            yVisited.add("x" + str(tailPosX[i]) + " y" + str(tailPosY[i]))
        elif direction_line == 'D':
            for down in range(int(step)):
                print("d", end='')
                printRope(tailPosX, tailPosY)
                headPosY -= 1
                tailPosY[0] = headPosY
                xVisited.add("x" + str(headPosX) + " y" + str(headPosY))
                direction = distancedFromHead(headPosX, headPosY, tailPosX[1], tailPosY[1])
                for i in range(1, len(tailPosX)):
                    if direction != DIRECTION.NO_MOVE:
                        tailPosY[i] = moveTail(tailPosY[i], direction)
                        tailPosX[i] = tailPosX[i - 1]
                        if i < len(tailPosX) - 1:
                            direction = distancedFromHead(tailPosX[i], tailPosY[i], tailPosX[i + 1], tailPosY[i + 1])
                        else:
                            yVisited.add("x" + str(tailPosX[i]) + " y" + str(tailPosY[i]))
    # print(xVisited)
    print("Part two:", len(yVisited))
