
import random

class Cloudlet():
    def __init__(self):

        self.position = random.randint(1,3)
        self.instructions = random.randint(1,300)
        self.size = random.randint(1,30)
        self.high_priority = random.randint(0,1)

        self.classLabel = int
        self.executionTime = int

    def getAsDict(self):
        """ returns the attributes and values of cloudlet in a dictionary

        Returns:
            [dict]: [attribute and values of the cloudlet]
        """

        dic = {}
        dic['position'] = self.position
        dic['instructions'] = self.instructions
        dic['size'] = self.size
        dic['high_priority'] = self.high_priority

        return dic

    def getCategorizedAsList(self):
        """ returns the attribute of cloudlet in a dictionary

        Returns:
            [list]: [attribute values of the cloudlet]
        """

        arr = []
        arr.append(self.position)

        if self.instructions <= 100:
            arr.append(0)
        else:
            arr.append(1)

        if self.instructions <= 10:
            arr.append(0)
        else:
            arr.append(1)

        arr.append(self.high_priority)

        return arr

    def clearHistory(self):
        self.executionTime = 0
        self.transferTime = 0
