#int - key, string - value

class HashTable:
    def __init__(self, sizeTable, currentCollisionsDecision):
        self.buffer = [None for _ in range (sizeTable)]
        self.sizeTable = sizeTable
        self.loadFactor = 0
        self.collisionsDecisions = ["LinearDecision",
                                    "QuadraticDecision",
                                    "TwiceHashDecision"]
        self.NameCurrentMethod = currentCollisionsDecision
        self.sumCollisions = 0


    def print(self):
        print(self.buffer)


    def simpleHashing(self, key):
        return key % self.sizeTable


    # def secondHashing(self, key):
    #     res = (key % (self.sizeTable - 1))
    #     if res % 2 == 0:
    #         res += 1
    #     return res


    def subHash(self, key):
        result = 0
        x = self.sizeTable - 1
        key = str(key)
        for i in range(len(key)):
            result = (x * result + int(key[i])) % self.sizeTable
        result = (result * 2 + 1) % self.sizeTable
        return result


    def CurrentMethod(self, key, curHashingResult, i):
        if self.NameCurrentMethod == self.collisionsDecisions[0]:
            curHashingResult = self.LinearMethod(key, curHashingResult, i)
        elif self.NameCurrentMethod == self.collisionsDecisions[1]:
            curHashingResult = self.QuadraticMethod(key, curHashingResult, i)
        elif self.NameCurrentMethod == self.collisionsDecisions[2]:
            curHashingResult = self.TwiceHashingMethod(key, curHashingResult, i)
        return curHashingResult



    def QuadraticMethod(self, key, curHashingResult, i): #i - номер шага
        curHashingResult = (curHashingResult + pow(i,2)) % self.sizeTable
        return curHashingResult


    def LinearMethod(self, key, curHashingResult, i):
        curHashingResult = (curHashingResult + i) % self.sizeTable
        return curHashingResult


    def TwiceHashingMethod(self, key, curHashingResult, i):
        curHashingResult = (curHashingResult + i*self.subHash(key)) % self.sizeTable
        return curHashingResult


    def Add(self, key, value):
        curHashingResult = self.simpleHashing(key)
        pair = [key, value]
        for i in range(self.sizeTable):
            if self.buffer[curHashingResult]:
                self.sumCollisions += 1
                curHashingResult = self.CurrentMethod(key, curHashingResult, i)
            else:
                self.buffer[curHashingResult] = pair
                self.loadFactor += 1
                break
        if (self.loadFactor/self.sizeTable)*100 > 80:
            # print(self.sizeTable, key)
            self.rehashing()
            # print(self.sizeTable, key)
            # pass



    def rehashing(self):
        lastSize = self.sizeTable
        self.sizeTable *= 2
        lastBuffer = self.buffer
        self.loadFactor = 0
        self.sumCollisions = 0
        self.buffer = [None for _ in range (self.sizeTable)]
        for i in range (lastSize):
            if lastBuffer[i]:
                self.Add(lastBuffer[i][0], lastBuffer[i][1])


    def find(self, key):  # return pair
        curHashingResult = self.simpleHashing(key)
        ans = "string"
        for i in range(self.sizeTable):
            if self.buffer[curHashingResult]:
                if self.buffer[curHashingResult][0] == key:
                    ans = self.buffer[curHashingResult]
                    break
                else:
                    curHashingResult = self.CurrentMethod(key, curHashingResult, i)
            else:
                ans = "element not found"
                break
        return ans



# hashTable = HashTable(8, "LinearDecision")
# hashTable.Add(9, "pop")
# hashTable.Add(2, "it")
# hashTable.Add(10, "kek")
# hashTable.Add(18, "lol")
# hashTable.Add(5, "boooo")
# print(hashTable.find(28))
# hashTable.print()




