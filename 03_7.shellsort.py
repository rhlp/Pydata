# [6,5,1,3,2,4]


def shell_sort(li):

    n = len(li)
    # 定义步长
    gap = n//2
    # 让步长由大变小，最后必须1步长
    while gap >= 1:

        # 按照步长，把数据分成两半，遍历后面一半数据
        for i in range(gap, n):
            # 当前位置，跟减去步长 找到前一个数，进行比较

            while (i-gap) >= 0:
                if li[i] < li[i-gap]:
                    li[i], li[i-gap] = li[i-gap], li[i]
                i -= gap
        gap //= 2


# ***
# **
# *

def t(n):
    if n == 0:
        return
    print("*" * n)
    t(n-1)

# 5 5+4+3+2+1


def t2(n):
    if n == 1:
        return 1
    return t2(n-1)+n

if __name__ == '__main__':
    print(t2(3))
    l = [6,5,5,3,7]
    # [1,3,2,4,6,5]
    # shell_sort(l)
    # print(l)

    # 时间复杂度： 跟步长有关
    # 稳定性： 不稳定

