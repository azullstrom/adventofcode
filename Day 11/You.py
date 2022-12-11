from Monkey import MONKEY_INFO_LINE_LENGTH


class You:
    def __init__(self):
        self.monkeyCount = 0
        self.oldWorryLevel = []
        self.newWorryLevel = []
        self.divider = 0

    def getMonkeyCount(self, lines):
        for line in lines:
            if line.__contains__('Monkey'):
                self.monkeyCount += 1
        return self.monkeyCount

    def getWorryLevel(self, text):
        worryLevel = []
        for i in range(2, len(text)):
            text[i] = text[i].replace(',', '')
            worryLevel.append(int(text[i]))
        return worryLevel

    def setOldWorryLevel(self, worryLevel):
        for i in worryLevel:
            self.oldWorryLevel.append(i)

    def setDivider(self, divider):
        self.divider = divider
