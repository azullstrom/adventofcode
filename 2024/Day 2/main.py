if __name__ == '__main__':
    input_file = 'input.txt'
    data = open(input_file).read().splitlines()
    rows = [list(map(int, row.split())) for row in data]

    part_one = 0
    for row in rows:
        ascending = row == sorted(row)
        descending = row == sorted(row, reverse=True)
        valid = all(1 <= abs(row[i+1] - row[i]) <= 3 for i in range(len(row) - 1))

        if (ascending or descending) and valid:
            part_one += 1
    print(part_one)
