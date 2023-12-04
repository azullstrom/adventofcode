input_file = 'input.txt'
data = open(input_file).read().split('\n')
arr = []
part_one = 0

for i in data:
    arr.append(i.split(' '))

for row in arr:
    right_side = False
    winning_temp = []
    your_temp = []
    for col in row:
        if col == '|':
            right_side = True
        if col.isdigit():
            if right_side:
                your_temp.append(col)
            else:
                winning_temp.append(col)
    win_set = set(winning_temp)
    your_set = set(your_temp)
    correct_set = win_set.intersection(your_set)
    temp = 0
    for i in range(len(correct_set)):
        if(temp == 0):
            temp = 1
        else:
            temp *= 2
    part_one += temp

print(part_one)
