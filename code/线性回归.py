# Linear regression
# Created by 敖鸥 at 2022/06/11
from typing import List, Any


class LinearRegression:
    parm: List[Any] = []

    def __init__(self, x: list, y: list, target=None, rate=1.0, parmN=2):
        """
        线性回归
        :param x: 自变量
        :param y: 因变量
        :param target: 回归函数
        :param rate: 学习率
        :param parmN: 参数个数
        """
        if len(x) == len(y):
            self.x = x
            self.y = y
            self.rate = rate
            self.target = target
            self.parmN = parmN
            self.parm = [1 for _ in range(parmN)]
            self.handler = [diff_liner1, diff_liner2]
        else:
            raise ValueError("输入长度不一致！")

    def train(self, loop=5000) -> list:
        for j in range(loop):
            temp = [i for i in self.parm]  # 用于同步更新参数
            for i in range(self.parmN):
                temp[i] = self.parm[i] - self.rate * self._main(self.handler[i])
            for i in range(self.parmN):
                self.parm[i] = temp[i]
        return self.parm

    def _main(self, handler):
        n = len(self.x)
        re = 0
        for i in range(n):
            re += handler(self.x[i], *self.parm) * (self._Target(self.x[i]) - self.y[i])
        return re / n

    def _Target(self, x):
        if self.target is None:
            return liner(x, *self.parm)
        else:
            return self.target(x, *self.parm)

    def set_parm(self, *parm):
        """
        设置参数初始值
        :param parm:
        :return:
        """
        if len(parm) >= self.parmN:
            for i in range(self.parmN):
                self.parm[i] = parm[i]
        else:
            raise ValueError("参数数目不足！")

    def set_handler(self, *func):
        """
        设置对各参数求导函数
        :param func:
        :return:
        """
        if len(func) == self.parmN:
            self.handler = []
            for i in func:
                self.handler.append(i)
        else:
            raise ValueError("参数数目不足！")

    def predict(self, x):
        return self._Target(x)


def liner(x, *parm):
    return parm[0] * x + parm[1]


def diff_liner1(x, *parm):
    return x


def diff_liner2(x, *parm):
    return 1


def two(x, *parm):
    return parm[0] * x * x + parm[1] * x + parm[2]


def diff_two1(x, *parm):
    return x * x


def diff_two2(x, *parm):
    return x


def diff_two3(x, *parm):
    return 1


# test2
def test2():
    x = [i + 1 for i in range(5)]
    y = [2 * i * i + 2 * i + 2 for i in x]
    T = LinearRegression(x, y, target=two, rate=0.001, parmN=3)
    T.set_handler(diff_two1, diff_two2, diff_two3)
    # T.set_parm(1.5, 1.5, 1.5)
    P = T.train(loop=100000)
    print(P)
    print(T.predict(7))


if __name__ == '__main__':
    # test1
    ll = LinearRegression([1, 2, 3, 4, 5],
                          [4, 6, 8, 10, 12], rate=0.09)
    parmP = ll.train(loop=10000)
    print(parmP)
    print(ll.predict(4))
    test2()
