import math

from Monkey import Monkey
from You import You

ROUNDS = 20


def updateLines(lines, i):
    if lines[i].__contains__('Operation'):
        text = lines[i - 1].strip().split()

        for i in range(2, len(text)):
            text[i] = str(you.newWorryLevel[i - 2])
        return text
    return False

if __name__ == '__main__':
    data = open('test.txt').read()
    lines = [x for x in data.split('\n')]

    you = You()
    monkey = []
    monkey_count = you.getMonkeyCount(lines)
    for i in range(monkey_count):
        monkey.append(Monkey(i))

    for i in range(ROUNDS):
        index = -1
        lineIndex = 0
        receivingMonkey = []
        for line in lines:
            if line.__contains__('Monkey'):
                index += 1
            elif line.__contains__('Starting items'):
                text = line.strip().split()
                worryLevel = you.getWorryLevel(text)
                you.setOldWorryLevel(worryLevel)
                monkey[index].setStartItems(worryLevel)
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
                if len(you.newWorryLevel) != monkey[index].itemCount:
                    you.newWorryLevel = []
                    for i in monkey[index].startingItems:
                        you.newWorryLevel.append(i)
                for i in range(len(you.newWorryLevel)):
                    you.newWorryLevel[i] = math.floor(you.newWorryLevel[i] / 3)
                    monkey[index].startingItems[i] = you.newWorryLevel[i]
                you.oldWorryLevel = []
            elif line.__contains__('Test'):
                text = line.strip().split()
                you.setDivider(int(text[3]))
            elif line.__contains__('true'):
                text = line.strip().split()
                for item in monkey[index].startingItems:
                    if item % you.divider == 0:
                        receivingMonkey.append(int(text[5]))
            elif line.__contains__('false'):
                text = line.strip().split()
                for item in monkey[index].startingItems:
                    if item % you.divider != 0:
                        receivingMonkey.append(int(text[5]))
            else:
                for i in range(len(monkey[index].startingItems)):
                    itemInAir = monkey[index].throwAway()
                    monkey[receivingMonkey[i]].catchItem(itemInAir)
                you.newWorryLevel = []
                receivingMonkey = []
            temp = updateLines(lines, lineIndex)
            if temp:
                line = temp
            lineIndex += 1

    monkeyInspectionList = []
    for i in monkey:
        print(i.startingItems)
        monkeyInspectionList.append(i.inspectedItems)
    print(monkeyInspectionList)
