# [5,1,3,2,4]


def insert_sort(li):

    n = len(li)
    # 依次把第二个数据到最后数据插入到前面的有序序列
    for j in range(1, n):

        # 认为第一个数有序， 从后面取一个数，倒着往前遍历，插入到前面的有序序列中
        for i in range(j, 0, -1):
            if li[i] < li[i-1]:
                li[i], li[i-1] = li[i-1], li[i]
            else:
                # 当前数据大于或者等于前面的数据是，不需要在往前面遍历
                break
if __name__ == '__main__':
    l = [5,1,3,2,4]
    insert_sort(l)
    print(l)

    # 最坏时间复杂度： O(n^2)
    # 最优时间复杂度： O(n)
    # 稳定性： 稳定