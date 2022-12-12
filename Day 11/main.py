import math

from Monkey import Monkey
from You import You

ROUNDS = 20


if __name__ == '__main__':
    data = open('input.txt').read()
    lines = [x for x in data.split('\n')]

    you = You()
    monkey = []
    monkey_count = you.getMonkeyCount(lines)
    for i in range(monkey_count):
        monkey.append(Monkey(i))

    index = 0
    for line in lines:
        if line.__contains__('Starting items'):
            text = line.strip().split()
            worryLevel = you.getWorryLevel(text)
            you.setOldWorryLevel(worryLevel)
            monkey[index].setStartItems(worryLevel)
            index += 1

    receivingMonkey = []
    for roundCount in range(ROUNDS):
        index = -1
        for line in lines:
            if line.__contains__('Monkey'):
                index += 1
            elif line.__contains__('Starting items'):
                you.oldWorryLevel = monkey[index].startingItems
            elif line.__contains__('Operation'):
                text = line.strip().split()
                for i in range(len(you.oldWorryLevel)):
                    if text[4] == '*':
                        if text[5] == 'old':
                            you.newWorryLevel.append(you.oldWorryLevel[i] * you.oldWorryLevel[i])
                        else:
                            you.newWorryLevel.append(you.oldWorryLevel[i] * int(text[5]))
                    elif text[4] == '+':
                        if text[5] == 'old':
                            you.newWorryLevel.append(you.oldWorryLevel[i] + you.oldWorryLevel[i])
                        else:
                            you.newWorryLevel.append(you.oldWorryLevel[i] + int(text[5]))
                temp = []
                for i in range(len(you.newWorryLevel)):
                    temp.append(you.newWorryLevel[i] // 3)
                monkey[index].startingItems = temp
                you.oldWorryLevel = []
            elif line.__contains__('Test'):
                text = line.strip().split()
                you.setDivider(int(text[3]))
            elif line.__contains__('true'):
                text = line.strip().split()
                you.divideTrue = int(text[5])
            elif line.__contains__('false'):
                text = line.strip().split()
                you.divideFalse = int(text[5])
            else:
                temp = [x for x in monkey[index].startingItems]
                for i in range(len(monkey[index].startingItems)):
                    itemInAir = monkey[index].throwAway()
                    if temp[i] % you.divider == 0:
                        monkey[you.divideTrue].catchItem(itemInAir)
                    else:
                        monkey[you.divideFalse].catchItem(itemInAir)
                you.newWorryLevel = []
                receivingMonkey = []

    monkeyInspectionList = []
    for i in monkey:
        monkeyInspectionList.append(i.inspectedItems)
    monkeyInspectionList.sort(reverse=True)
    print("part one: ", monkeyInspectionList[0] * monkeyInspectionList[1], monkeyInspectionList)
