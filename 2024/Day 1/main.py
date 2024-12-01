if __name__ == '__main__':
    input_file = 'input.txt'
    data = open(input_file).read().split()

    left_col = data[::2]
    right_col = data[1::2]

    left_sorted = sorted(left_col)
    right_sorted = sorted(right_col)

    both_sorted = list(zip(left_sorted, right_sorted))

    part_one = 0
    for i, data in enumerate(both_sorted):
        part_one += abs(int(data[0]) - int(data[1]))

    print(part_one)


        
