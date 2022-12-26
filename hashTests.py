import time
from hash import HashTable
from random import randrange
import matplotlib.pyplot as plt

#реализовать худший случай - одинаковые жлементы
#средний - рандомные
#лучший - последовательные

def TheWorstCase():
    addX = []
    addY = []
    diffrentSizes = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2500, 3000, 3500, 4000]
    for size in range (len(diffrentSizes)):
        newTable = HashTable(128, "LinearDecision", "TheWorstHashEVER")
        tic = time.perf_counter_ns()
        addX.append(diffrentSizes[size])
        for i in range (diffrentSizes[size]):
                newTable.Add(i, str(i))
        toc = time.perf_counter_ns()
        timee = (toc - tic)/diffrentSizes[size]
        addY.append(timee)


    findX = []
    findY = []
    for size in range(len(diffrentSizes)):
        newTable1 = HashTable(128, "LinearDecision", "TheWorstHashEVER") #тут нет разницы, какой хеш, сравниваем время поиска
        findX.append(diffrentSizes[size])
        for i in range (diffrentSizes[size]-1):
            newTable1.Add(i, str(i))
        newTable1.Add(12345, str(12345))
        tictic = time.perf_counter_ns()
        newTable1.find(12345)
        # newTable1.find(randrange(diffrentSizes[size]))
        toctoc = time.perf_counter_ns()
        newtime = (toctoc - tictic)
        findY.append(newtime)

    ans = []
    ans.append(addX)
    ans.append(addY)
    ans.append(findX)
    ans.append(findY)
    return ans

def TheMiddleCase():
    addX = []
    addY = []

    diffrentSizes = [i * 10000 for i in range(1,15)]

    for size in range(len(diffrentSizes)):
        newTable = HashTable(20, "QuadraticDecision", "SimpleHash")
        tic = time.perf_counter_ns()
        addX.append(diffrentSizes[size])
        for i in range(diffrentSizes[size]):
            newTable.Add(randrange(10000000000), str(randrange(10000000000)))  # cредний случай
        toc = time.perf_counter_ns()
        timee = (toc - tic) / diffrentSizes[size]
        addY.append(timee)

    findX = []
    findY = []
    for size in range(len(diffrentSizes)):
        newTable1 = HashTable(128, "QuadraticDecision",
                              "SimpleHash")  # тут нет разницы, какой хеш, сравниваем время поиска
        findX.append(diffrentSizes[size])
        for i in range(diffrentSizes[size]):
            newTable1.Add(i, str(i))
        tictic = time.perf_counter_ns()
        newTable1.find(randrange(diffrentSizes[size]))
        toctoc = time.perf_counter_ns()
        newtime = (toctoc - tictic)
        findY.append(newtime)

    ans = []
    ans.append(addX)
    ans.append(addY)
    ans.append(findX)
    ans.append(findY)
    return ans

def TheBestCase():
    addX = []
    addY = []
    diffrentSizes = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000,
                     140000, 150000]
    for size in range(len(diffrentSizes)):
        newTable = HashTable(128, "QuadraticDecision", "SimpleHash")
        tic = time.perf_counter_ns()
        addX.append(diffrentSizes[size])
        for i in range(diffrentSizes[size]):
            newTable.Add(i, str(i))  # cредний случай
        toc = time.perf_counter_ns()
        timee = (toc - tic) / diffrentSizes[size]
        addY.append(timee)

    findX = []
    findY = []
    for size in range(len(diffrentSizes)):
        newTable1 = HashTable(128, "QuadraticDecision",
                              "SimpleHash")  # тут нет разницы, какой хеш, сравниваем время поиска
        findX.append(diffrentSizes[size])
        for i in range(diffrentSizes[size]):
            newTable1.Add(i, str(i))
        tictic = time.perf_counter_ns()
        newTable1.find(randrange(diffrentSizes[size]))
        toctoc = time.perf_counter_ns()
        newtime = (toctoc - tictic)
        findY.append(newtime)

    ans = []
    ans.append(addX)
    ans.append(addY)
    ans.append(findX)
    ans.append(findY)
    return ans


def Research(typeOfCase):
    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.suptitle("Исследование сложности операций с хеш таблицей")  # заголовок
    ax2.set_xlabel("Количесво элементов")  # ось абсцисс
    ax1.set_ylabel("Время, нс")  # ось ординат
    ax1.grid()  # включение отображение сетки
    ax2.grid()
    if typeOfCase == "TheWorst":
        Parametrs = TheWorstCase()
        ax1.plot(Parametrs[0], Parametrs[1], color="red")  # построение графика
        ax2.plot(Parametrs[2], Parametrs[3], color="red")  # построение графика
        ax1.legend(["Сложность добавления в худшем случае"])
        ax2.legend(["Сложность поиска в худшем случае"])
    elif typeOfCase == "Middle":
        Parametrs = TheMiddleCase()
        ax1.plot(Parametrs[0], Parametrs[1], 'b')  # построение графика
        ax2.plot(Parametrs[2], Parametrs[3], color="blue")  # построение графика
        ax1.legend(["Сложность добавления в среднем случае"])
        ax2.legend(["Сложность поиска в среднем случае"])
    else:
        Parametrs = TheBestCase()
        ax1.plot(Parametrs[0], Parametrs[1], color="green")  # построение графика
        ax2.plot(Parametrs[2], Parametrs[3], color="green")  # построение графика
        ax1.legend(["Сложность добавления в лучшем случае"])
        ax2.legend(["Сложность поиска в лучшем случае"])
    plt.show()

