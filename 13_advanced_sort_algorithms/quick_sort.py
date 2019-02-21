# coding:utf-8
# @Time : 2019/2/20 18:27 
# @Author : Andy.Zhang
# @Desc : 快速排序


def quick_sort(array):  # T(n) = 2T(n/2)+n = (n * logn)
    """
    快速排序
    缺点：
        1、需要额外存储空间，less_part, great_part，增加了额外的存储空间
        2、partition：左/右组合元素的时候实现了两次遍历，如果元素量级大这样也会增加时间复杂度
    :param array:
    :return:
    """
    if len(array) < 2:
        return array
    else:
        pivot_index = 0
        pivot = array[pivot_index]
        less_part = [i for i in array[pivot_index + 1:] if i <= pivot]
        great_part = [i for i in array[pivot_index + 1:] if i > pivot]
        return quick_sort(less_part) + [pivot] + quick_sort(great_part)


def partition(array, began, end):
    """
    对给定数组执行 partition操作，返回新的pivot位置
    :param array:
    :param began:
    :param end:
    :return:
    """
    pivot_index = began
    pivot = array[pivot_index]
    left = pivot_index + 1
    right = end - 1  # 开区间，最后一个元素位置是 end-1

    while True:
        # 从左边找到比 pivot 大的元素
        while left <= right and array[left] < pivot:
            left += 1

        # 从右边找到比 pivot 小的元素，然后与上面找到的左边比 pivot 大的元素交换
        while left <= right and array[right] >= pivot:
            right -= 1

        if left > right:
            break  # 说明一轮循环已经走完了
        else:
            array[left], array[right] = array[right], array[left]  # 这样交换后保证左边的元素永远比 pivot小，右边比其大
    array[pivot_index], array[right] = array[right], array[pivot_index]  # 最后把pivot放到它的合适位置中，即比左边的大，比右边的小
    # 因为此时的 array[right]已是上面循环一轮指针再往左移一位置的元素，所以其实是属于左边区的最后一个比pivot小的元素，交换后就左,pivot，右
    return right  # 新的 pivot位置 （即： right >= left 才 break)


def quick_sort_inplace(array, began, end):  # 左闭右开区间
    """
    快排改良版，从左边开始逐渐找到最合适的元素排序，边排边往右边靠拢
    :param array:
    :param began:
    :param end:
    :return:
    """
    if began < end:
        pivot = partition(array, began, end)
        quick_sort_inplace(array, began, pivot)
        quick_sort_inplace(array, pivot+1, end)


def test_quick_part():
    import random
    array = list(range(10))
    random.shuffle(array)
    assert quick_sort(array) == sorted(array)

    assert partition([4, 1, 2, 8], 0, 4) == 2
    assert partition([1, 2, 3, 4], 0, 4) == 0
    assert partition([4, 3, 2, 1], 0, 4) == 3
    assert partition([1], 0, 1) == 0
    assert partition([2, 1], 0, 2) == 1

    import random
    array = list(range(10))
    random.shuffle(array)
    array_old = array
    quick_sort_inplace(array, 0, len(array))
    assert array_old == array


if __name__ == '__main__':
    test_quick_part()
