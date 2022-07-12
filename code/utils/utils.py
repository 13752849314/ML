# Created by 敖鸥 at 2022/6/12

def hg(n, *f):  # test
    for i in f:
        print(i)
    print(n)


def dot(x: list, y: list) -> float:
    """
    点乘
    :param x:
    :param y:
    :return: x.y
    """
    if len(x) == len(y):
        re = 0.0
        for i in range(len(x)):
            re += x[i] * y[i]
        return re
    else:
        raise ValueError('参数长度不一致!')


if __name__ == '__main__':
    L = [i + 1 for i in range(6)]
    hg(1, 2, 3, 7)
    print(L)
    for i in range(len(L)):
        L[i] = L[i] + 1
    print(L)
    print(dot(L, L))
