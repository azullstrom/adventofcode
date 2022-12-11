MONKEY_INFO_LINE_LENGTH = 7


class Monkey:
    def __init__(self, id):
        self.id = id
        self.startingItems = []
        self.inspectedItems = 0
        self.itemCount = 0

    def printSelf(self):
        print(self.id, self.startingItems)

    def appendItem(self, item):
        self.startingItems.append(item)

    def throwAway(self):
        self.itemCount -= 1
        return self.startingItems.pop(0)

    def setStartItems(self, startItems):
        for i in startItems:
            self.startingItems.append(i)
            self.inspectedItems += 1
            self.itemCount += 1

    def catchItem(self, itemInAir):
        self.startingItems.append(itemInAir)
        self.inspectedItems += 1
        self.itemCount += 1
