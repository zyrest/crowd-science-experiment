import numpy as np

datas = [
        [(1, 2), (1, 6), (1, 7), (2, 3), (2, 6), (3, 6), (3, 7), (4, 5), (4, 7), (5, 6), (6, 7)],

        [(1, 2), (1, 3), (1, 6), (1, 7), (2, 3), (2, 5), (2, 6), (3, 6), (3, 7), (4, 5), (4, 6),
         (4, 7), (5, 6), (5, 7), (6, 7)],

        [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 3), (2, 5), (2, 6), (2, 7), (3, 5),
         (3, 6), (3, 7), (4, 5), (4, 6), (4, 7), (5, 6), (5, 7), (6, 7)]
]
size = 7


def array2matrix(array):
    ans = np.zeros([size, size], dtype='i')
    for p in array:
        x_ = p[0]
        y_ = p[1]
        ans[x_ - 1][y_ - 1] = 1
        ans[y_ - 1][x_ - 1] = 1
    return np.array(ans)


def mark_friend(known, dot):
    for tri in range(size):
        dot[tri][tri] = -1

    for kn in known:
        x_ = kn[0]
        y_ = kn[1]
        dot[x_ - 1][y_ - 1] = -1
        dot[y_ - 1][x_ - 1] = -1


# 将数据转化为邻接矩阵
matrix = []
for i in range(len(datas)):
    matrix.append(array2matrix(datas[i]))
    # print(matrix[i])


commons = []
dots = []
for v in range(len(datas) - 1):
    commonFriend = []
    for c in range(size + 1):
        commonFriend.append(0)
    # 将当前邻接矩阵相乘，[a,b]=3表示a与b在当前快照不是朋友，他们的共同朋友个数为3。等于0的是当前已经是朋友，或是没有共同好友
    dotMatrix = np.dot(matrix[v], matrix[v])
    # 标记出当前已经是朋友的pair，用-1表示
    mark_friend(datas[v], dotMatrix)
    dots.append(dotMatrix)
    # print(dotMatrix)

    # 统计当前有{pair}个共同好友的pair个数
    for line in dotMatrix:
        for pair in line:
            if pair != -1:
                commonFriend[pair] += 1

    for c in range(size + 1):
        commonFriend[c] //= 2
    commons.append(commonFriend)

# print(commons)
# print(dots)
newAdd = []
for n in range(1, len(datas)):
    d = dots[n-1]
    mat = matrix[n]
    new = []
    for c in range(size + 1):
        new.append(0)
    for x in range(size):
        for y in range(size):
            if d[x][y] != -1 and mat[x][y] != 0:
                new[d[x][y]] += 1

    for c in range(size + 1):
        new[c] //= 2
    newAdd.append(new)

# print(newAdd)
for t in range(len(datas) - 1):
    prob = []
    new = newAdd[t]
    common = commons[t]
    for index in range(len(new)):
        if common[index] != 0:
            prob.append(new[index] / common[index])
        else:
            prob.append(0.0)

    print("第%d快照与第%s快照之间成为朋友的概率：" % (t+1, t+2))
    print(prob)
