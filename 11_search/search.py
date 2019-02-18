# coding:utf-8
# @Time : 2019/2/18 22:50 
# @Author : Andy.Zhang
# @Desc : 性线查找(遍历)与二分查询，linear search and binary search


def linear_search(value, iterable):
    for index, val in enumerate(iterable):
        if val == value:  # found
            return index
    else:
        return -1  # not found


def linear_search_v2(predicate, iterable):
    for index, val in enumerate(iterable):
        if predicate(val):
            return index
    else:
        return -1


def linear_search_recursive(array, value):  # 递归查找
    if len(array) == 0:
        return -1

    index = len(array) - 1
    if array[index] == value:
        return index
    else:
        return linear_search_recursive(array[0:index], value)


# 二分查找在另外一个图解算法项目里面已经写了，这里就不再重复了。后续有空再把添加进来。


def test_search():
    number_list = [0, 1, 2, 3, 4, 5, 6, 7]
    assert linear_search(5, number_list) == 5
    assert linear_search_v2(lambda x: x == 5, number_list) == 5
    assert linear_search_recursive(number_list, 5) == 5
    assert linear_search_recursive(number_list, 8) == -1
    assert linear_search_recursive(number_list, 7) == 7
    assert linear_search_recursive(number_list, 0) == 0

