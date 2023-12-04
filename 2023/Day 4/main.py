from collections import defaultdict

input_file = 'input.txt'
data = open(input_file).read().split('\n')
arr = []
part_one = 0
instances = defaultdict(int)

for i in data:
    arr.append(i.split(' '))

for game_num, row in enumerate(arr, 1):
    right_side = False
    winning_temp = []
    your_temp = []
    instances[game_num] += 1
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
    for j, _ in enumerate(correct_set, 1):
        instances[game_num+j] += instances[game_num]
        if(temp == 0):
            temp = 1
        else:
            temp *= 2
    part_one += temp
part_two = sum(instances.values())
print(part_one, part_two)
