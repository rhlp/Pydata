# 搜索


def search(li, item):

    # 停止条件
    if len(li) == 0:
        return False

    # 获取一半的位置
    mid = len(li)//2

    # 比较要找到的数据和中间数的大小
    if item == li[mid]:
        return True
    elif item > li[mid]:
        return search(li[mid+1:], item)
    else:
        return search(li[:mid], item)

if __name__ == '__main__':

    l = [1,2,3,4,5,6]
    print(search(l,2))
    print(search(l,4))
    print(search(l,6))
    print(search(l,0))

