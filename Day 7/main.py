from collections import defaultdict

if __name__ == '__main__':
    input_file = 'input.txt'
    data = open(input_file).read().strip()
    lines = [x for x in data.split('\n')]

    size_dict = defaultdict(int)
    path = []
    for line in lines:
        # Dividing line into three elements
        words = line.strip().split()

        if words[1] == 'cd':
            if words[2] == '..':
                # Popping to change current directory
                path.pop()
            else:
                # Appending to change current directory
                path.append(words[2])
        elif words[1] == 'ls':
            continue
        elif words[0] == 'dir':
            continue
        else:
            file_size = int(words[0])
            for i in range(1, len(path) + 1):
                # Adding file_size to current directory size and all parent's directory size
                size_dict['/'.join(path[:i])] += file_size
    part_one = 0
    total_size = 70000000
    needed_size = 30000000
    available_size = total_size - size_dict['/']
    need_to_free = needed_size - available_size
    current_free = total_size

    for index, value in size_dict.items():
        if value <= 100000:
            part_one += value
        if value >= need_to_free:
            if value < current_free:
                current_free = value
    part_two = current_free

    print(part_one)
    print(part_two)
