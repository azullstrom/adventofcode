import re

if __name__ == '__main__':
    input_file = 'input.txt'
    data = open(input_file).read()

    matches = re.findall(r"mul\((\d+),(\d+)\)", data)

    part_one = 0
    results = [int(a) * int(b) for a, b in matches]

    for number in results:
        part_one += number

    print(part_one)
