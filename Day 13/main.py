import re


if __name__ == '__main__':
    data = open("test.txt").read()
    E = [x for x in data.split('\n')]
    print(E)
    P_1 = 0
    PAIR = 1

    ROW = len(E)
    for row in range(ROW - 1):
        COL_FIRST = len(E[row])
        COL_SECOND = len(E[row + 1])
        COL = min(COL_FIRST, COL_SECOND)
        for col in range(COL):
            if row % 3 == 0:
                print(PAIR, "first:", E[row][col], "second:", E[row + 1][col])
                if E[row][col] == '[' and E[row + 1][col] == '[':
                    continue
                elif E[row][col] == ',' and E[row + 1][col] == ',':
                    continue
                elif E[row][col] == '[' and re.match("[0-9]", E[row+1][col]):
                    E[row+1] = E[row+1][:col] + '[' + E[row+1][col] + E[row+1][col+2:]
                    continue
                elif re.match("[0-9]", E[row][col]) and E[row+1][col] == '[':
                    E[row] = E[row][:col] + '[' + E[row][col] + E[row][col+2:]
                    continue
                elif re.match("[0-9]", E[row][col]) and re.match("[0-9]", E[row+1][col]):
                    if col == COL_FIRST - 1 and not int(E[row][col]) > int(E[row+1][col]):
                        P_1 += PAIR
                        print(P_1)
                        continue
                    if int(E[row][col]) < int(E[row+1][col]):
                        P_1 += PAIR
                        print(P_1)
                        break
                    elif int(E[row][col]) > int(E[row+1][col]):
                        break
                elif re.match("[^-0-9/]+", E[row][col]) or re.match("[^-0-9/]+", E[row+1][col]):
                    if col == COL_FIRST - 1:
                        P_1 += PAIR
                        print(P_1)
        if row % 3 == 0:
            PAIR += 1
    print(P_1)
