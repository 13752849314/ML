# Linear regression
# Created by 敖鸥 at 2022/06/11
class LinearRegression:
    parm1 = 1
    parm2 = 1

    def __init__(self, x: list, y: list, rate=1):
        if len(x) == len(y):
            self.x = x
            self.y = y
            self.rate = rate
        else:
            raise ValueError("输入长度不一致！")

    def train(self, loop=500) -> list:
        for i in range(loop):
            self.parm1 = self.parm1 - self.rate * self._Parm1()
            self.parm2 = self.parm2 - self.rate * self._Parm2()
        return [self.parm1, self.parm2]

    def _Target(self, x):
        return self.parm1 * x + self.parm2

    def _Penalty(self):
        m = len(self.x)
        J = 0.0
        for i in range(m):
            J += (self._Target(self.x[i]) - self.y[i]) ** 2
        return J / (2 * m)

    def _Parm2(self):
        m = len(self.x)
        re = 0.0
        for i in range(m):
            re += self._Target(self.x[i]) - self.y[i]
        return re / m

    def _Parm1(self):
        m = len(self.x)
        re = 0.0
        for i in range(m):
            re += (self._Target(self.x[i]) - self.y[i]) * self.x[i]
        return re / m

    def set_parm(self, parm1, parm2):
        self.parm1 = parm1
        self.parm2 = parm2

    def predict(self, x):
        return self.parm1 * x + self.parm2


if __name__ == '__main__':
    ll = LinearRegression([1, 2, 3], [-1, -2, -3])
    parm = ll.train()
    print(parm)
    print(ll.predict(11))
