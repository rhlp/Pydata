# [6,9,4,8,5,7]


def merge_sort(li):
    # 停止条件
    if len(li) == 1:
        # print(li)
        return li

    # 根据长度计算中间位置
    mid = len(li)//2

    # 使用切片把数据变成两半
    left = li[:mid]
    right = li[mid:]

    # print(left)
    # print(right)

    # 递归拆分数据
    left_res = merge_sort(left)
    right_res = merge_sort(right)
    # res = left_res + right_res
    # 把下层的结果组成有序序列
    res = merge(left_res,right_res)
    # 把下层方法返回的两个结果，合并再返回给上层方法
    # print(res)
    return res


def merge(l,r):
    """把两个有序序列，再组成有序序列"""
    # [9] [4]
    # [6] [4,9]
    # [4,6,9] [5,7,8]

    # 定义两个下标，分别从0位置开始
    l_index = 0
    r_index = 0

    # 定义临时列表，存结果
    result = []
    while l_index < len(l) and r_index < len(r):

        if l[l_index] <= r[r_index]:
            result.append(l[l_index])
            l_index += 1
        else:
            result.append(r[r_index])
            r_index += 1
    result += l[l_index:]
    result += r[r_index:]
    return result

if __name__ == '__main__':
    l = [6,5,4,3,2]

    print(merge_sort(l))
    # print(l)

    # lef = [4, 6, 9]
    # rig = [5, 7, 8,10]
    # print(merge(lef,rig))

    # 最坏时间复杂度： O(nlogn)
    # 最好时间复杂度： O(nlogn)
    # 稳定性：稳定

