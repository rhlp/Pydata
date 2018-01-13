# [5,1,3,2,4]

# temp = 1

def select_sort(li):

    n = len(li)

    # 每次选择一个最小的数，放到0到n-1位置
    for j in range(n-1):

        # 记录0位置的数据，认为0位置的数据最小
        temp = j

        # 依次跟后面的数据比较
        for i in range(j+1, n):
            if li[i] < li[temp]:
                # 把更小的数的位置 记录起来
                temp = i

        # 循环结束时，temp指向的是最小的位置
        li[temp], li[j] = li[j], li[temp]

if __name__ == '__main__':
    l = [5,1,3,2,4]
    select_sort(l)
    print(l)

    # 最坏时间复杂度： O(n^2)
    # 最优时间复杂度： O(n^2)
    # 稳定性： 不稳定

