# coding:utf-8
# @Time : 2019/2/20 18:27 
# @Author : Andy.Zhang
# @Desc : 快速排序


def quick_sort(array):
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


def test_quick_part():
    import random
    array = list(range(10))
    random.shuffle(array)
    assert quick_sort(array) == sorted(array)


if __name__ == '__main__':
    test_quick_part()
