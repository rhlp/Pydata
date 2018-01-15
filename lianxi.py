# [5,1,3,2,4]

# 冒泡排序
def bubble_sort(li):
    n = len(li)

    for j in range(n-1):
        flag=0
        for i in range(n-1-j):
            if li[i] > li[i+1]:
                li[i], li[i+1] = li[i+1], li[i]
                flag += 1

        if flag == 0:
            break

# if __name__ == '__main__':
    # l = [5,1,3,2,4]
    # bubble_sort(l)
    # print(l)


# 选择排序
def select_sort(li):
    n = len(li)

    for j in range(n-1):

        temp = j
        for i in range(j+1,n):
            if li[i] < li[temp]:
                temp = i

        li[temp], li[j] = li[j], li[temp]

# if __name__ == '__main__':
#     l = [5, 1, 3, 2, 4]
#     select_sort(l)
#     print(l)


# 插入排序
def insert_sort(li):
    n = len(li)

    for j in range(0,n):

        for i in range(j, 0, -1):
            if li[i] < li[i-1]:
                li[i], li[i-1] = li[i-1], li[i]

            else:
                break
if __name__ == '__main__':
    l  = [5, 1, 3, 2, 4]
    insert_sort(l)
    print(l)
