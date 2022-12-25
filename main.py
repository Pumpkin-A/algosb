from hash import HashTable
from hashTests import Research
from random import randrange


if __name__ == "__main__":
    hashTable = HashTable(64, "LinearDecision")
    hashTable.Add(9, "pop")
    hashTable.Add(2, "it")
    hashTable.Add(10, "kek")
    hashTable.Add(18, "lol")
    hashTable.Add(5, "boooo")
    print(hashTable.find(5))
    # for i in range (9930):
    #     hashTable.Add(randrange(10000000000), str(randrange(10000000000)))
    hashTable.print()
    Research(hashTable)