import time
from hash import HashTable
from random import randrange
import matplotlib.pyplot as plt

#реализовать худший случай - одинаковые жлементы
#средний - рандомные
#лучший - последовательные


def Research(hashTable):
    x = []
    y = []
    diffrentSizes = [10000,20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000]
    for size in range (len(diffrentSizes)):
        newTable = HashTable(128, "LinearDecision")
        tic = time.perf_counter_ns()
        x.append(diffrentSizes[size])
        for i in range (diffrentSizes[size]):
            newTable.Add(randrange(10000000000), str(randrange(10000000000))) #cредний случай
            # hashTable.Add(i, str(i))
        toc = time.perf_counter_ns()
        timee = (toc - tic)/diffrentSizes[size]
        y.append(timee)


    xx = []
    yy = []
    for size in range(len(diffrentSizes)):
        newTable1 = HashTable(128, "LinearDecision")
        tictic = time.perf_counter_ns()
        xx.append(diffrentSizes[size])
        for i in range (diffrentSizes[size]):
            newTable1.Add(randrange(10000000000), str(randrange(10000000000))) #cредний случай
        newTable1.Add(123456789, 'ertyuio')
        newTable1.find(123456789)
        toctoc = time.perf_counter_ns()
        newtime = (toctoc - tictic)/diffrentSizes[size]
        yy.append(newtime)
    # toc = time.perf_counter_ns()
    # # return [f"Вычисление заняло {toc - tic:0.4f} секунд", hashTable.sumCollisions]
    # timee = toc - tic


    # f1 = plt.subplot(2, 1, 2)
    # f2 = plt.subplot(2, 1, 1)
    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.suptitle("Исследование сложности операций с хеш таблицей в среднем случае")  # заголовок

    #x - count of elements
    #y - time
    # x = [i for i in range(50)]
    # y = x
    ax2.set_xlabel("Количесво элементов")  # ось абсцисс
    ax1.set_ylabel("Время, нс")  # ось ординат
    ax1.grid() # включение отображение сетки
    ax2.grid()
    ax1.plot(x, y, color="green")  # построение графика
    ax2.plot(xx, yy, color="blue")  # построение графика
    ax1.legend(["Сложность добавления в среднем случае"])
    ax2.legend(["Сложность поиска в среднем случае"])

    # ax1.show()
    plt.show()