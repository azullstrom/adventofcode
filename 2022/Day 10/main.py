def check_cycle(cycle):
    if (cycle % 40) - 20 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    data = open("input.txt").read()
    lines = [x for x in data.split('\n')]
    cycle = 0
    summary = 0
    part_one = 0

    for line in lines:
        cmd = num = ''
        if line.__contains__(" "):
            cmd, num = line.strip().split()
        else:
            cmd = line

        if cmd == 'noop':
            cycle += 1
            if check_cycle(cycle):
                part_one += (summary + 1) * cycle
        elif cmd == 'addx':
            for i in range(2):
                cycle += 1
                if check_cycle(cycle):
                    part_one += (summary + 1) * cycle
            summary += int(num)
    print(part_one)
