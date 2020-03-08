def binary_chop(alist, data):
    """
    非递归解决二分查找
    :param alist:
    :return:
    """
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (last + first) // 2
        if alist[mid] > data:
            last = mid - 1
        elif alist[mid] < data:
            first = mid + 1
        else:
            return True
    return False

#######################
####第三次修改
###master change

#快速排序
def quick_sort(L):
    return q_sort(L, 0, len(L) - 1)

def q_sort(L, left, right):
    if left < right:
        pivot = Partition(L, left, right)

        q_sort(L, left, pivot - 1)
        q_sort(L, pivot + 1, right)
    return L

def Partition(L, left, right):
    pivotkey = L[left]

    while left < right:
        while left < right and L[right] >= pivotkey:
            right -= 1
        L[left] = L[right]
        while left < right and L[left] <= pivotkey:
            left += 1
        L[right] = L[left]

    L[left] = pivotkey
    print(L)
    return left

L = [5, 9, 1, 11, 6, 7, 2, 4]

print(quick_sort(L))
