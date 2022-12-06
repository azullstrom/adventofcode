import re


if __name__ == '__main__':
    file = open('input.txt', 'r')
    input_file = file.readlines()
    pairs = 0
    pairs_two = 0

# Part 1
    for i in range(len(input_file)):
        input_file[i] = input_file[i].replace('\n', '')
        sections = re.split(r',|-', input_file[i])

        if int(sections[0]) <= int(sections[2]) <= int(sections[1]) and int(sections[1]) >= int(sections[3]) >= int(sections[0]):
            pairs += 1
        elif int(sections[2]) <= int(sections[0]) <= int(sections[3]) and int(sections[3]) >= int(sections[1]) >= int(sections[2]):
            pairs += 1
# Part 2
        if int(sections[0]) <= int(sections[2]) <= int(sections[1]) or int(sections[1]) >= int(sections[3]) >= int(sections[0]):
            pairs_two += 1
        elif int(sections[2]) <= int(sections[0]) <= int(sections[3]) or int(sections[3]) >= int(sections[1]) >= int(sections[2]):
            pairs_two += 1

    print(pairs, pairs_two)



