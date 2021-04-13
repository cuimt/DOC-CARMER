import time
import linecache
import matplotlib.pyplot as plt


def backpack(number, weight, w, v):
    # 初始化二维数组，用于记录背包中个数为i，重量为j时能获得的最大价值
    result = [[0 for i in range(weight + 1)] for i in range(number + 1)]
    # 循环将数组进行填充
    for i in range(1, number + 1):
        for j in range(1, weight + 1):
            if j < w[i - 1]:
                result[i][j] = result[i - 1][j]
            else:
                result[i][j] = max(result[i - 1][j], result[i - 1][j - w[i - 1]] + v[i - 1])
    return result


def main():
    number = 30
    weight = 10149

    the_profit = linecache.getline('C://Users//86138//Desktop//大三第二学期//软件工程//实验二 任务3data_set//idkp1-10.txt', 6)
    the_weight = linecache.getline('C://Users//86138//Desktop//大三第二学期//软件工程//实验二 任务3data_set//idkp1-10.txt', 8)

    the_profit1 = the_profit.split(',')
    the_weight1 = the_weight.split(',')
    the_profit1.remove('\n')
    the_weight1.remove('\n')
    the_profit2 = list(map(int, the_profit1))
    the_weight2 = list(map(int, the_weight1))
    profit_weight = [a / b for a, b in zip(the_weight2, the_profit2)]
    profit_weight3 = []

    print("价值为：")
    print(str(the_profit1) + "\n")

    print("重量为：")
    print(str(the_weight1) + "\n")
    print("价值/重量为：")
    print(str(profit_weight) + "\n")
    for i in profit_weight:
        j = round(i, 3)
        profit_weight3.append(j)
    print("价值/重量（保留三位小数）排序结果为：")
    print(str(profit_weight3) + "\n")

    start = time.time()
    result = backpack(number, weight, the_weight2, the_profit2, )
    end = time.time()
    print("动态规划算法：")
    print("共耗时:\n" + str(end - start) + " s")
    print("最优解为：" + str(result[number][weight]) + "\n")
    print("所选取的物品为：")
    item = [0 for i in range(number + 1)]
    j = weight
    for i in range(1, number + 1):
        if result[i][j] > result[i - 1][j]:
            item[i - 1] = 1
            j -= the_weight2[i - 1]
    for i in range(number):
        if item[i] == 1:
            print("第" + str(i + 1) + "件")            
    plt.xlim(xmax=1500, xmin=0)
    plt.ylim(ymax=1500, ymin=0)
    plt.plot(the_profit2, the_weight2, 'ro')
    plt.show()


if __name__ == '__main__':
    main()

