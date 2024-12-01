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

    part_two = 0
    for i in left_sorted:
        sum = 0
        for j in right_sorted:
            if j in i:
                sum += 1
        part_two += int(i) * sum

    print(part_one)
    print(part_two)


        
