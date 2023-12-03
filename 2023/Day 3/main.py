input_file = 'input.txt'
data = open(input_file).read().split()

rows = len(data)
cols = len(data[0])

matrix = [[0 for x in range(rows)] for y in range(cols)]

for i in range(rows):
    for j in range(cols):
        matrix[i][j] = data[i][j]

part_one = 0
prev_was_num = False
for i in range(rows):
    for j in range(cols):
        if not prev_was_num:
            number_str = ''
            symbol = False
            for k in range(j, rows):
                if matrix[i][k].isdigit():
                    number_str += str(matrix[i][k])
            
                    # down [i+1][j], right [i][j+1], down/right [i+1][j+1]
                    if i == 0 and k == 0:
                        if symbol is False:
                            symbol = matrix[i+1][k] != '.' or (matrix[i][k+1] != '.' and not matrix[i][k+1].isdigit()) or matrix[i+1][k+1] != '.'
                    # down [i+1][j], left [i][j-1], down/left [i+1][j-1]
                    elif i == 0 and k == (cols - 1):
                        if symbol is False:
                            symbol = matrix[i+1][k] != '.' or (matrix[i][k-1] != '.' and not matrix[i][k-1].isdigit()) or matrix[i+1][k-1] != '.'
                    # down [i+1][j], left [i][j-1], right [i][j+1], down/left [i+1][j-1], down/right [i+1][j+1]
                    elif i == 0:
                        if symbol is False:
                            symbol = matrix[i+1][k] != '.' or (matrix[i][k-1] != '.' and not matrix[i][k-1].isdigit()) or (matrix[i][k+1] != '.' and not matrix[i][k+1].isdigit()) or matrix[i+1][k-1] != '.' or matrix[i+1][k+1] != '.'
                    # down [i+1][j], right[i][j+1], up [i-1][j], down/right [i+1][j+1], up/right [i-1][j+1]
                    elif k == 0:
                        if symbol is False:
                            symbol = matrix[i+1][k] != '.' or (matrix[i][k+1] != '.' and not matrix[i][k+1].isdigit()) or matrix[i-1][k] != '.' or matrix[i+1][k+1] != '.' or matrix[i-1][k+1] != '.'
                    # down [i+1][j], left [i][j-1], up [i-1][j], down/left [i+1][j-1], up/left [i+1][j-1]
                    elif k == (cols - 1):
                        if symbol is False:
                            symbol = matrix[i+1][k] != '.' or (matrix[i][k-1] != '.' and not matrix[i][k-1].isdigit()) or matrix[i-1][k] != '.' or matrix[i+1][k-1] != '.' or matrix[i-1][k-1] != '.'
                    # up [i-1][j], right [i][j+1], up/right [i-1][j+1]
                    elif i == (rows - 1) and k == 0:
                        if symbol is False:
                            symbol = matrix[i-1][k] != '.' or (matrix[i][k+1] != '.' and not matrix[i][k+1].isdigit()) or matrix[i-1][k+1] != '.'
                    # up [i-1][j], left [i][j-1], up/left [i-1][j-1]
                    elif i == (rows - 1) and k == (cols - 1):
                        if symbol is False:
                            symbol = matrix[i-1][k] != '.' or (matrix[i][k-1] != '.' and not matrix[i][k-1].isdigit()) or matrix[i-1][k-1] != '.'
                    # up [i-1][j], left [i][j-1], right [i][j+1], up/left [i-1][j-1], up/right [i-1][j+1]
                    elif i == (rows - 1):
                        if symbol is False:
                            symbol = matrix[i-1][k] != '.' or (matrix[i][k-1] != '.' and not matrix[i][k-1].isdigit()) or (matrix[i][k+1] != '.' and not matrix[i][k+1].isdigit()) or matrix[i-1][k-1] != '.' or matrix[i-1][k+1] != '.'
                    # up, left, right, down, up/left, up/right, down/left, down/right
                    else:
                        if symbol is False:
                            symbol = matrix[i-1][k] != '.' or (matrix[i][k-1] != '.' and not matrix[i][k-1].isdigit()) or (matrix[i][k+1] != '.' and not matrix[i][k+1].isdigit()) or matrix[i+1][k] != '.' or matrix[i-1][k-1] != '.' or matrix[i-1][k+1] != '.' or matrix[i+1][k-1] != '.' or matrix[i+1][k+1] != '.'
                    
                    if (k == (cols - 1)) and matrix[i][k].isdigit():
                        if symbol:
                            part_one += int(number_str)
                        symbol = False
                        j = 0
                        break
                else:
                    if symbol:
                        part_one += int(number_str)
                    symbol = False
                    break
        prev_was_num = matrix[i][j].isdigit()

print(part_one)
