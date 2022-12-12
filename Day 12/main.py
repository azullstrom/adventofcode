

def moveShortest(steps, path, startRow, startCol, letter, prevRow, prevCol, avoidRow, avoidCol):
    print(path[startRow][startCol], startRow, startCol, letter)
    if path[startRow][startCol] == 'z' and path[startRow].__contains__('E'):
        letter = 'E'
        print(letter)
    if path[startRow][startCol] == 'E':
        return steps

    skipDown = skipUp = skipLeft = skipRight = False
    if startRow + 1 in avoidRow and startCol in avoidCol:
        skipDown = True
    elif startRow - 1 in avoidRow and startCol in avoidCol:
        skipUp = True
    elif startRow in avoidRow and startCol + 1 in avoidCol:
        skipRight = True
    elif startRow in avoidRow and startCol - 1 in avoidCol:
        skipLeft = True

    if 0 < startRow < len(path) - 1 and 0 < startCol < len(path[0]) - 1:
        print("if 0")
        if path[startRow + 1][startCol] == letter and not skipDown:
            return moveShortest(steps + 1, path, startRow + 1, startCol, chr(ord(letter) + 1), startRow, startCol, avoidRow, avoidCol)
        elif path[startRow][startCol + 1] == letter and not skipRight:
            return moveShortest(steps + 1, path, startRow, startCol + 1, chr(ord(letter) + 1), startRow, startCol, avoidRow, avoidCol)
        elif path[startRow - 1][startCol] == letter and not skipUp:
            return moveShortest(steps + 1, path, startRow - 1, startCol, chr(ord(letter) + 1), startRow, startCol, avoidRow, avoidCol)
        elif path[startRow][startCol - 1] == letter and not skipLeft:
            return moveShortest(steps + 1, path, startRow, startCol - 1, chr(ord(letter) + 1), startRow, startCol, avoidRow, avoidCol)
        # If no next letter search current
        elif path[startRow + 1][startCol] == chr(ord(letter) - 1) and startRow + 1 != prevRow and not skipDown:
            return moveShortest(steps + 1, path, startRow + 1, startCol, chr(ord(letter)), startRow, startCol, avoidRow, avoidCol)
        elif path[startRow][startCol + 1] == chr(ord(letter) - 1) and startCol + 1 != prevCol and not skipRight:
            return moveShortest(steps + 1, path, startRow, startCol + 1, chr(ord(letter)), startRow, startCol, avoidRow, avoidCol)
        elif path[startRow - 1][startCol] == chr(ord(letter) - 1) and startRow - 1 != prevRow and not skipUp:
            return moveShortest(steps + 1, path, startRow - 1, startCol, chr(ord(letter)), startRow, startCol, avoidRow, avoidCol)
        elif path[startRow][startCol - 1] == chr(ord(letter) - 1) and startCol - 1 != prevCol and not skipLeft:
            return moveShortest(steps + 1, path, startRow, startCol - 1, chr(ord(letter)), startRow, startCol, avoidRow, avoidCol)
        # If dead end
        avoidRow.append(startRow)
        avoidCol.append(startCol)
        return False
    elif startRow == 0 and 0 < startCol < len(path[0]) - 1:
        print("if 1")
        if path[startRow + 1][startCol] == letter and not skipDown:
            return moveShortest(steps + 1, path, startRow + 1, startCol, chr(ord(letter) + 1), startRow, startCol,
                                avoidRow, avoidCol)
        elif path[startRow][startCol + 1] == letter and not skipRight:
            return moveShortest(steps + 1, path, startRow, startCol + 1, chr(ord(letter) + 1), startRow, startCol,
                                avoidRow, avoidCol)
        elif path[startRow][startCol - 1] == letter and not skipLeft:
            return moveShortest(steps + 1, path, startRow, startCol - 1, chr(ord(letter) + 1), startRow, startCol,
                                avoidRow, avoidCol)
        # If no next letter search current
        elif path[startRow + 1][startCol] == chr(ord(letter) - 1) and startRow + 1 != prevRow and not skipDown:
            return moveShortest(steps + 1, path, startRow + 1, startCol, chr(ord(letter)), startRow, startCol, avoidRow,
                                avoidCol)
        elif path[startRow][startCol + 1] == chr(ord(letter) - 1) and startCol + 1 != prevCol and not skipRight:
            return moveShortest(steps + 1, path, startRow, startCol + 1, chr(ord(letter)), startRow, startCol, avoidRow,
                                avoidCol)
        elif path[startRow][startCol - 1] == chr(ord(letter) - 1) and startCol - 1 != prevCol and not skipLeft:
            return moveShortest(steps + 1, path, startRow, startCol - 1, chr(ord(letter)), startRow, startCol, avoidRow,
                                avoidCol)
        # If dead end
        avoidRow.append(startRow)
        avoidCol.append(startCol)
        return False
    elif startCol == 0 and 0 < startRow < len(path) - 1:
        print("if 2")
        if path[startRow + 1][startCol] == letter and not skipDown:
            return moveShortest(steps + 1, path, startRow + 1, startCol, chr(ord(letter) + 1), startRow, startCol,
                                avoidRow, avoidCol)
        elif path[startRow][startCol + 1] == letter and not skipRight:
            return moveShortest(steps + 1, path, startRow, startCol + 1, chr(ord(letter) + 1), startRow, startCol,
                                avoidRow, avoidCol)
        elif path[startRow - 1][startCol] == letter and not skipUp:
            return moveShortest(steps + 1, path, startRow - 1, startCol, chr(ord(letter) + 1), startRow, startCol,
                                avoidRow, avoidCol)
        # If no next letter search current
        elif path[startRow + 1][startCol] == chr(ord(letter) - 1) and startRow + 1 != prevRow and not skipDown:
            return moveShortest(steps + 1, path, startRow + 1, startCol, chr(ord(letter)), startRow, startCol, avoidRow,
                                avoidCol)
        elif path[startRow][startCol + 1] == chr(ord(letter) - 1) and startCol + 1 != prevCol and not skipRight:
            return moveShortest(steps + 1, path, startRow, startCol + 1, chr(ord(letter)), startRow, startCol, avoidRow,
                                avoidCol)
        elif path[startRow - 1][startCol] == chr(ord(letter) - 1) and startRow - 1 != prevRow and not skipUp:
            return moveShortest(steps + 1, path, startRow - 1, startCol, chr(ord(letter)), startRow, startCol, avoidRow,
                                avoidCol)
        # If dead end
        avoidRow.append(startRow)
        avoidCol.append(startCol)
        return False
    elif startRow == len(path) - 1 and 0 < startCol < len(path[0]) - 1:
        print("if 3")
        if path[startRow][startCol + 1] == letter and not skipRight:
            return moveShortest(steps + 1, path, startRow, startCol + 1, chr(ord(letter) + 1), startRow, startCol,
                                avoidRow, avoidCol)
        elif path[startRow - 1][startCol] == letter and not skipUp:
            return moveShortest(steps + 1, path, startRow - 1, startCol, chr(ord(letter) + 1), startRow, startCol,
                                avoidRow, avoidCol)
        elif path[startRow][startCol - 1] == letter and not skipLeft:
            return moveShortest(steps + 1, path, startRow, startCol - 1, chr(ord(letter) + 1), startRow, startCol,
                                avoidRow, avoidCol)
        # If no next letter search current
        elif path[startRow][startCol + 1] == chr(ord(letter) - 1) and startCol + 1 != prevCol and not skipRight:
            return moveShortest(steps + 1, path, startRow, startCol + 1, chr(ord(letter)), startRow, startCol, avoidRow,
                                avoidCol)
        elif path[startRow - 1][startCol] == chr(ord(letter) - 1) and startRow - 1 != prevRow and not skipUp:
            return moveShortest(steps + 1, path, startRow - 1, startCol, chr(ord(letter)), startRow, startCol, avoidRow,
                                avoidCol)
        elif path[startRow][startCol - 1] == chr(ord(letter) - 1) and startCol - 1 != prevCol and not skipLeft:
            return moveShortest(steps + 1, path, startRow, startCol - 1, chr(ord(letter)), startRow, startCol, avoidRow,
                                avoidCol)
        # If dead end
        avoidRow.append(startRow)
        avoidCol.append(startCol)
        return False
    elif startCol == len(path[0]) - 1 and 0 < startRow < len(path) - 1:
        print("if 4")
        if path[startRow + 1][startCol] == letter and not skipDown:
            return moveShortest(steps + 1, path, startRow + 1, startCol, chr(ord(letter) + 1), startRow, startCol,
                                avoidRow, avoidCol)
        elif path[startRow - 1][startCol] == letter and not skipUp:
            return moveShortest(steps + 1, path, startRow - 1, startCol, chr(ord(letter) + 1), startRow, startCol,
                                avoidRow, avoidCol)
        elif path[startRow][startCol - 1] == letter and not skipLeft:
            return moveShortest(steps + 1, path, startRow, startCol - 1, chr(ord(letter) + 1), startRow, startCol,
                                avoidRow, avoidCol)
        # If no next letter search current
        elif path[startRow + 1][startCol] == chr(ord(letter) - 1) and startRow + 1 != prevRow and not skipDown:
            return moveShortest(steps + 1, path, startRow + 1, startCol, chr(ord(letter)), startRow, startCol, avoidRow,
                                avoidCol)
        elif path[startRow - 1][startCol] == chr(ord(letter) - 1) and startRow - 1 != prevRow and not skipUp:
            return moveShortest(steps + 1, path, startRow - 1, startCol, chr(ord(letter)), startRow, startCol, avoidRow,
                                avoidCol)
        elif path[startRow][startCol - 1] == chr(ord(letter) - 1) and startCol - 1 != prevCol and not skipLeft:
            return moveShortest(steps + 1, path, startRow, startCol - 1, chr(ord(letter)), startRow, startCol, avoidRow,
                                avoidCol)
        # If dead end
        avoidRow.append(startRow)
        avoidCol.append(startCol)
        return False
    elif startRow == 0 and startCol == 0:
        print("if 5")
        if path[startRow + 1][startCol] == letter and not skipDown:
            return moveShortest(steps + 1, path, startRow + 1, startCol, chr(ord(letter) + 1), startRow, startCol,
                                avoidRow, avoidCol)
        elif path[startRow][startCol + 1] == letter and not skipRight:
            return moveShortest(steps + 1, path, startRow, startCol + 1, chr(ord(letter) + 1), startRow, startCol,
                                avoidRow, avoidCol)
        # If no next letter search current
        elif path[startRow + 1][startCol] == chr(ord(letter) - 1) and startRow + 1 != prevRow and not skipDown:
            return moveShortest(steps + 1, path, startRow + 1, startCol, chr(ord(letter)), startRow, startCol, avoidRow,
                                avoidCol)
        elif path[startRow][startCol + 1] == chr(ord(letter) - 1) and startCol + 1 != prevCol and not skipRight:
            return moveShortest(steps + 1, path, startRow, startCol + 1, chr(ord(letter)), startRow, startCol, avoidRow,
                                avoidCol)
        # If dead end
        avoidRow.append(startRow)
        avoidCol.append(startCol)
        return False
    elif startRow == len(path) - 1 and startCol == len(path[0]) - 1:
        print("if 6")
        if path[startRow - 1][startCol] == letter and not skipUp:
            return moveShortest(steps + 1, path, startRow - 1, startCol, chr(ord(letter) + 1), startRow, startCol,
                                avoidRow, avoidCol)
        elif path[startRow][startCol - 1] == letter and not skipLeft:
            return moveShortest(steps + 1, path, startRow, startCol - 1, chr(ord(letter) + 1), startRow, startCol,
                                avoidRow, avoidCol)
        # If no next letter search current
        elif path[startRow - 1][startCol] == chr(ord(letter) - 1) and startRow - 1 != prevRow and not skipUp:
            return moveShortest(steps + 1, path, startRow - 1, startCol, chr(ord(letter)), startRow, startCol, avoidRow,
                                avoidCol)
        elif path[startRow][startCol - 1] == chr(ord(letter) - 1) and startCol - 1 != prevCol and not skipLeft:
            return moveShortest(steps + 1, path, startRow, startCol - 1, chr(ord(letter)), startRow, startCol, avoidRow,
                                avoidCol)
        # If dead end
        avoidRow.append(startRow)
        avoidCol.append(startCol)
        return False
    elif startRow == len(path) - 1 and startCol == 0:
        print("if 7")
        if path[startRow][startCol + 1] == letter and not skipRight:
            return moveShortest(steps + 1, path, startRow, startCol + 1, chr(ord(letter) + 1), startRow, startCol,
                                avoidRow, avoidCol)
        elif path[startRow - 1][startCol] == letter and not skipUp:
            return moveShortest(steps + 1, path, startRow - 1, startCol, chr(ord(letter) + 1), startRow, startCol,
                                avoidRow, avoidCol)
        # If no next letter search current
        elif path[startRow][startCol + 1] == chr(ord(letter) - 1) and startCol + 1 != prevCol and not skipRight:
            return moveShortest(steps + 1, path, startRow, startCol + 1, chr(ord(letter)), startRow, startCol, avoidRow,
                                avoidCol)
        elif path[startRow - 1][startCol] == chr(ord(letter) - 1) and startRow - 1 != prevRow and not skipUp:
            return moveShortest(steps + 1, path, startRow - 1, startCol, chr(ord(letter)), startRow, startCol, avoidRow,
                                avoidCol)
        # If dead end
        avoidRow.append(startRow)
        avoidCol.append(startCol)
        return False
    elif startCol == len(path[0]) - 1 and startRow == 0:
        print("if 8")
        if path[startRow + 1][startCol] == letter and not skipDown:
            return moveShortest(steps + 1, path, startRow + 1, startCol, chr(ord(letter) + 1), startRow, startCol,
                                avoidRow, avoidCol)
        elif path[startRow][startCol - 1] == letter and not skipLeft:
            return moveShortest(steps + 1, path, startRow, startCol - 1, chr(ord(letter) + 1), startRow, startCol,
                                avoidRow, avoidCol)
        # If no next letter search current
        elif path[startRow + 1][startCol] == chr(ord(letter) - 1) and startRow + 1 != prevRow and not skipDown:
            return moveShortest(steps + 1, path, startRow + 1, startCol, chr(ord(letter)), startRow, startCol, avoidRow,
                                avoidCol)
        elif path[startRow][startCol - 1] == chr(ord(letter) - 1) and startCol - 1 != prevCol and not skipLeft:
            return moveShortest(steps + 1, path, startRow, startCol - 1, chr(ord(letter)), startRow, startCol, avoidRow,
                                avoidCol)
        # If dead end
        avoidRow.append(startRow)
        avoidCol.append(startCol)
        return False


if __name__ == '__main__':
    data = open("input.txt").read()
    lines = [x for x in data.split('\n')]
    startRow = startCol = 0

    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == 'S':
                startRow = row
                startCol = col
    #print(startRow, startCol)
    avoidRow = []
    avoidCol = []
    steps = False
    while not steps:
        print(steps)
        steps = moveShortest(0, lines, startRow, startCol, 'a', -2, -2, avoidRow, avoidCol)

    print(steps, avoidRow, avoidCol)

