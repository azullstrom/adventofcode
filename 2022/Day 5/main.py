import re

def replace_newline(arr):
    for i in range(len(arr)):
        arr[i] = arr[i].replace('\n', '')

    return arr

def split_numbers(arr):
    for i in range(len(arr)):
        arr[i] = re.findall(r'\d+', arr[i])

    return arr


if __name__ == '__main__':
    procedure_file = open('procedure.txt', 'r')
    procedure = procedure_file.readlines()
    procedure = split_numbers(procedure)
    crates_file = open('crates.txt')
    crates = crates_file.readlines()
    crates = replace_newline(crates)
    arr = []

# Part 1
    for i in range(len(crates) - 1):
        temp_str = ''
        j = 0
        arr.append([])
        for letter in crates[i]:
            temp_str += letter
            if j % 4 == 3:
                arr[i].append(temp_str)
                temp_str = ''
            j += 1

    sorted_crates = []
    for i in range(len(arr) + 1):
        sorted_crates.append([])
        for j in range(len(arr)):
            sorted_crates[i].append(arr[j].pop(0))

    sorted_without_empty = []
    for i in range(len(sorted_crates)):
        sorted_without_empty.append([name for name in sorted_crates[i] if name.strip()])

    # Move crates
    for arr in procedure:
        for i in range(int(arr[0])):
            if len(sorted_without_empty[int(arr[1]) - 1]) > 0:
                temp = sorted_without_empty[int(arr[1]) - 1].pop(0)
                sorted_without_empty[int(arr[2]) - 1].insert(0, temp)
    # Print top of stacks
    for arr in sorted_without_empty:
        print(arr[0], end='')
    print('')

# Part 2
    sorted_without_empty = []
    for i in range(len(sorted_crates)):
        sorted_without_empty.append([name for name in sorted_crates[i] if name.strip()])

    # Move multiple crates (in same order as it was)
    for arr in procedure:
        j = int(arr[0]) - 1
        for i in range(int(arr[0])):
            if len(sorted_without_empty[int(arr[1]) - 1]) > 0 and j < len(sorted_without_empty[int(arr[1]) - 1]):
                temp = sorted_without_empty[int(arr[1]) - 1].pop(j)
                sorted_without_empty[int(arr[2]) - 1].insert(0, temp)
            j -= 1
    # Print top of stacks
    for arr in sorted_without_empty:
        print(arr[0], end='')
    print('')

