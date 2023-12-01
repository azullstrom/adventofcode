import dictionary


def get_duplicates(a, b):
    set1 = set(a)
    set2 = set(b)
    duplicates = set1.intersection(set2)
    list_dup = list(duplicates)

    return list_dup


def get_duplicates_three(a, b, c):
    set1 = set(a)
    set2 = set(b)
    set3 = set(c)
    duplicates = set1.intersection(set2.intersection(set3))
    list_dup = list(duplicates)

    return list_dup


def split_string(value):
    string1, string2 = value[:len(value)//2], value[len(value)//2:]

    return string1, string2


if __name__ == '__main__':
    file = open('input.txt', 'r')
    input_file = file.readlines()

    summary = 0
    # Part 1
    for i in range(len(input_file)):
        input_file[i] = input_file[i].replace('\n', '')
        one, two = split_string(input_file[i])
        duplicate = get_duplicates(one, two)

        for j in range(len(duplicate)):
            summary += dictionary.rucksack[duplicate[j]]
    print(summary)

    # Part 2
    summary = 0

    for i in range(len(input_file)):
        if i % 3 == 0:
            three_elves = []
            for j in range(i, i + 3):
                three_elves.append(input_file[j])
            duplicates = get_duplicates_three(three_elves[0], three_elves[1], three_elves[2])
            for j in range(len(duplicates)):
                summary += dictionary.rucksack[duplicates[j]]
    print(summary)
