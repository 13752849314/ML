# Created by 敖鸥 at 2022/6/12

def hg(n, *f):
    for i in f:
        print(i)
    print(n)


if __name__ == '__main__':
    L = [i + 1 for i in range(6)]
    hg(1, 2, 3, 7)
    print(L)
    for i in range(len(L)):
        L[i] = L[i] + 1
    print(L)
