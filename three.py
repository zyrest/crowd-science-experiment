import numpy as np


def ajm2probm():
    trans = np.transpose(m)
    ans = np.zeros(m.shape, dtype=float)
    for i in range(len(m)):
        for j in range(len(m[i])):
            ans[i][j] = m[i][j] / (trans[j].sum())
    # print(ans)
    return ans


# 有向图的邻接矩阵
m = np.array([[0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
              [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
              [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 1, 0, 0, 0, 0]],
             dtype=float)
# 浏览当前网页的概率
p = 0.85
# 将邻接矩阵转化为 （a，b）-> 由b到a点的概率
probm = ajm2probm()
# 存储每次结果的矩阵， 初始值为 1/n
ansm = np.zeros((m.shape[0], 1), dtype=float)
for i in range(len(m)):
    ansm[i] = 1 / len(m)


def page_rank():
    ret = p * np.dot(probm, ansm) + (1 - p) * ansm
    if (ret == ansm).all():
        print("ok")
    return ret


time = 0
while time < 20:
    ansm = page_rank()
    print("第%s次计算后结果为：" % (time+1))
    print(ansm)
    time += 1
