# coding:utf-8
# @Time : 2019/2/19 20:25 
# @Author : Andy.Zhang
# @Desc : 高级排序，例如merge_sort归并排序


def merge_sort(array):
    """
    归并排序，先将一个序列从中间劈开成两部分，再两部分里面递归劈开4部分，每个递归的出口是元素只有一个时才返回
    :param array:
    :return:
    """
    if len(array) <= 1:  # 只有一个元素是递归出口
        return array
    else:
        mid = int(len(array)/2)
        left_half = merge_sort(array[:mid])
        right_half = merge_sort(array[mid:])

        # 合并两个有序的数组:
        new_array = merge_sorted_list(left_half, right_half)
        return new_array


def merge_sorted_list(sorted_a, sorted_b):
    """
    合并两个有序序列，返回一个新的有序序列
    :param sorted_a:
    :param sorted_b:
    :return:
    """
    length_a, length_b = len(sorted_a), len(sorted_b)
    a = b = 0
    new_sorted_array = list()

    while a < length_a and b < length_b:
        if sorted_a[a] < sorted_b[b]:
            new_sorted_array.append(sorted_a[a])
            a += 1
        else:
            new_sorted_array.append(sorted_b[b])
            b += 1

    # 如果 a或b 中还有剩余元素，需要放到最后 (不可能 a和b同时 <，因为上面的 while 条件已经排除了这种情况，所以下面两个if永远只可能中命中一个)
    if a < length_a:
        new_sorted_array.extend(sorted_a[a:])
    if b < length_b:
        new_sorted_array.extend(sorted_b[b:])

    return new_sorted_array


def test_merge_sort():
    import random
    array = list(range(10))
    random.shuffle(array)
    assert merge_sort(array) == sorted(array)


if __name__ == '__main__':
    test_merge_sort()