# Created by 敖鸥 at 2022/7/12
from code.utils.utils import hg, dot
from math import e


class Logistic:
    def __init__(self, x: list, y: list, rate=1.0, target=None, parmN=2):
        if len(x) == len(y):
            self.x = x
            self.y = y
            self.rate = rate
            self.target = target
            self.parmN = parmN
            self.parm = [1.0 for _ in range(self.parmN)]
        else:
            raise ValueError('参数长度不一致!')

    def set_parm(self, *parm):
        if len(parm) >= self.parmN:
            for i in range(self.parmN):
                self.parm[i] = parm[i]
        else:
            raise ValueError('参数不足!')

    def train(self, loop=10000) -> list:
        temp = [0.0 for i in range(self.parmN)]
        for k in range(loop):
            for i in range(self.parmN):
                temp[i] = self.parm[i] - self.rate * self._main(i)
            for i in range(self.parmN):
                self.parm[i] = temp[i]
        return self.parm

    def _target(self, x):
        if self.target is None:
            temp = dot(x, self.parm)
            return sigmoid(temp)
        else:
            return sigmoid(self.target(x, self.parm))

    def _main(self, j):
        n = len(self.x)
        re = 0.0
        for i in range(n):
            re += self.x[i][j] * (self._target(self.x[i]) - self.y[i])
        return re

    def predict(self, x):
        return self._target(x)


def sigmoid(x):
    return 1 / (1 + e ** (-x))


if __name__ == '__main__':
    hg(5, 1, 2, 3)
    print(sigmoid(1234))
    x1 = [0.5, 1, 2, 1, 0, 1, 0, 2, 0, 3, 3, 2, 3, 1, 2, 1, 2]
    x2 = [0.5, 1, 0.5, 1.5, 0, 0, 1, 0, 2, 3, 0, 2, 1, 3, 3, 2, 1]
    print(len(x1))
    x = [[1, x1[i], x2[i]] for i in range(len(x1))]
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    L = Logistic(x, y, parmN=3, rate=0.0003)
    print(L.train())
    print(L.predict([1, 2, -1]))
