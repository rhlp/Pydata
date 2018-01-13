# [5,1,3,2,4]


def bubble_sort(li):

    n = len(li)
    # 共排序的趟数， n-1

    for j in range(n-1):
        # 遍历列表，让下标从0取到倒数第二个位置
        # 一趟冒泡，让最大的数移动到最右边

        flag = 0
        for i in range(n-1-j):  # 没一趟遍历的次数比前一趟少一次
            # 拿当前位置的数与下一个进行比较
            if li[i] > li[i+1]:
                li[i], li[i+1] = li[i+1], li[i]
                flag += 1

        # 内层循环遍历一次后，如果从来没有交换过，证明列表已经有序
        if flag == 0:
            break

if __name__ == '__main__':
    l = [5,1,3,2,4]
    bubble_sort(l)

    print(l)

    # 最坏时间复杂度： O(n^2)
    # 最优时间复杂度： O(n)
    # 稳定性： 稳定
