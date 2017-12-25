import matplotlib.pyplot as plt
import random
import numpy as np


class SchellingModel(object):

    # 需要参数，方块的长宽length
    def __init__(self, length, t):
        self.matrix = np.zeros(length * length).reshape((length, length))
        self.t = t  # 阀值 [0，9]
        self.space = 0  # 0代表当前位置没有人
        self.red = 1  # 红和蓝各代表两类不同的人
        self.blue = 2
        self.length = length
        self.population = 0  # 人口总数
        for i in range(length):
            for j in range(length):
                self.matrix[i][j] = random.randint(0, 2)  # 对于地图随机赋值，0,1,2
                if self.matrix[i][j] != 0:  # 说明该地方有人
                    self.population += 1

    def is_satisfied(self, i, j, kind):
        same_neighbour = -1  # 除了（i，j）本身
        # 选取（i，j）附近3*3的方格区域
        neighbour_matrix = self.matrix[i-1 if i-1 >= 0 else 0:i+2, j-1 if j-1 >= 0 else 0:j+2]
        # 数出当前区域有多少个同类
        for i in range(len(neighbour_matrix)):
            for j in range(len(neighbour_matrix[i])):
                if neighbour_matrix[i][j] == kind:
                    same_neighbour += 1
        # 判断是否大于阀值
        if same_neighbour >= self.t:
            return True
        else:
            return False

    # 为不满意的点随机取一个搬家位置
    def random_find(self):
        i = random.randint(0, self.length-1)
        j = random.randint(0, self.length-1)
        while self.matrix[i][j] != 0:
            i = random.randint(0, self.length - 1)
            j = random.randint(0, self.length - 1)
        return i, j

    # 主要方法，迭代当前地图所有点，判断居民是否满意，不满意搬走
    def move(self):
        satisfy = 0
        for i in range(self.length):
            for j in range(self.length):
                if self.matrix[i][j] != self.space:
                    people_kind = self.matrix[i][j]
                    judge = self.is_satisfied(i, j, people_kind)
                    if judge == 0:
                        (p, q) = self.random_find()
                        self.matrix[p][q] = people_kind
                        self.matrix[i][j] = self.space
                    else:
                        satisfy += 1
        return satisfy

    # 可视化方法
    def draw(self, time, satisfy=0):
        redx = []
        bluex = []
        redy = []
        bluey = []
        for i in range(self.length):
            for j in range(self.length):
                if self.matrix[i][j] == self.blue:
                    bluex.append(i)
                    bluey.append(j)
                elif self.matrix[i][j] == self.red:
                    redx.append(i)
                    redy.append(j)
        plt.scatter(redx, redy, c='r', marker='.', linewidths=0)
        plt.scatter(bluex, bluey, c='b', marker='.', linewidths=0)
        if satisfy == 0:
            plt.title('Initial')
        else:
            title = str(time)+' times satisfy:'+str(float(satisfy)/float(self.population))
            plt.title(title)
        plt.show()


if __name__ == '__main__':
    s = SchellingModel(150, 4)
    s.draw(0)
    i = 0
    while i < 100:
        satisfy = s.move()
        i += 1
        s.draw(i, satisfy)
