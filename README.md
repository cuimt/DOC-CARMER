# DOC-CARMER
Cmt的仓库
#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np



with open('idkp1-10.txt','r') as file:
    file.seek(1814)
    xstr_weight1=file.read(1279)
    x1_list= xstr_weight1.split(',')
    
    file.close()
    
with open('idkp1-10.txt','r') as file:
    file.seek(554)
    ystr_profit1=file.read(1231)
    y1_list=ystr_profit1.split(',')
    file.close()

with open('sdkp1-10.txt','r') as file:
    file.seek(1477)
    xstr_weight2=file.read(1208)
    x2_list= xstr_weight2.split(',')
    file.close()
    
with open('sdkp1-10.txt','r') as file:
    file.seek(168)
    ystr_profit2=file.read(1280)
    y2_list=ystr_profit2.split(',')
    file.close()

print("第一组数据的重量为：")
for item1 in x1_list:
    print(item1,end=" ")

print("\n第一组数据的价值为：\n")
for item2 in y1_list:
    print(item2,end=" ")

print("\n第二组数据的重量为：")
for item3 in x2_list:
    print(item3,end=" ")

print("\n第二组数据的价值为：\n")
for item4 in y2_list:
    print(item4,end=" ")


plt.scatter(x1_list, y1_list, marker = '*',color = 'blue', s = 3 ,label = 'First set of data')
#                   记号形状       颜色           点的大小    设置标签
plt.scatter(x2_list, y2_list, marker = '*', color = 'red', s = 3, label = 'Second set of data')
plt.legend(loc = 'best')    # 设置 图例所在的位置 使用推荐位置

plt.show()


def bag(n, c, w, v):
    """
    测试数据：
    n = 300  物品的数量，
    c = 61500 书包能承受的重量，
    w = x1_list 每个物品的重量，
    v = y1_list 每个物品的价值
    """
    # 置零，表示初始状态
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            value[i][j] = value[i - 1][j]
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i - 1]] + v[i - 1]:
                value[i][j] = value[i - 1][j - w[i - 1]] + v[i - 1]
    for x in value:
        print(x)
    return value

def show(n, c, w, value):
    print('最大价值为:', value[n][c])
    x = [False for i in range(n)]
    j = c
    for i in range(n, 0, -1):
        if value[i][j] > value[i - 1][j]:
            x[i - 1] = True
            j -= w[i - 1]
    print('背包中所装物品为:')
    for i in range(n):
        if x[i]:
            print('第', i+1, '个,', end='')

def bag1(n, c, w, v):
    values = [0 for i in range(c+1)]
    for i in range(1, n + 1):
        for j in range(c, 0, -1):
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            if j >= w[i-1]:
                values[j] = max(values[j-w[i-1]]+v[i-1], values[j])
    return values


if __name__ == '__main__':
    n = 300
    c = 61500
    w = x1_list
    v = y1_list
    value = bag(n, c, w, v)
    
    
    show(n, c, w, value)
   


  
