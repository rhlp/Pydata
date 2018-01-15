# 快速排序

def quick_sort(li, start, end):

    # 递归结束条件
    if start >= end:
        return

    # 定义两个下标
    low = start
    high = end

    # 取左边下标位置的数，作为中间值
    mid = li[low]

    while low < high:

        # 右边的下标往左移动，找到小于mid的数据，放到low位置
        while low < high and li[high] >= mid:
            high -= 1
        # 找到小于mid的数据放到low位置
        li[low] = li[high]

        # 左边的下标往右移动，找到大于mid的数据，放到high位置
        while low < high and li[low] < mid:
            low += 1
        # 找到大于扥大于mid的数据，放到high位置
        li[high] = li[low]

    # 当循环结束时，low=high，把mid数据放到次位置
    li[low] = mid

    # 循环继续排序左边和右边的数据
    quick_sort(li, start, low-1)
    quick_sort(li, low+1, end)

if __name__ == '__main__':

    l = [6,5,4,3,2]
    quick_sort(l,0,len(l)-1)
    print(l)

    # 最坏时间复杂度： O(n^2)
    # 最优时间复杂度： O(nlogn)
    # 稳定性： 不稳定


