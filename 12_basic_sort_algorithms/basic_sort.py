# coding:utf-8
# @Time : 2019/2/18 23:28 
# @Author : Andy.Zhang
# @Desc : 常见基本排序算法


import random


def bubble_sort(array):  # O(n^2)，准确的效率为：(n-1) * n/2，所以粗略记作 O(n^2)
    """冒泡排序
    1、外层进行 n个元素-1次循环
    2、每次内层循环所，前后元素对比，把大的放后放，以至于每轮循环都是把当前元素最大的放后面
    """
    if not array:
        return array

    print('\n bubble sort')
    array_length = len(array)
    for i in range(array_length-1):  # 外层共进行 length -1 次循环（因为最后一次已经排好了，所以就可以少一次循环）
        print('step %s:' % (i+1), array)  # 通过每次外层循环后打印出数组的变化，可以看出每次把当前最大的元素放到后面去了
        for j in range(array_length - i - 1):  # 内层每次循环都需要 减掉之前已排过的元素，所以需要 - i
            if array[j] > array[j+1]:  # 如果前一个元素 > 后一个元素，交换位置，保证了最大的永远能排到后面去
                array[j+1], array[j] = array[j], array[j+1]


def selection_sort(array):  # O(n^2)，和冒泡效率一样
    """选择排序
    和冒泡差不多思路，只不过冒泡是每次把最大元素放到后面合适的位置，选择排序是每次把最小的元素放前面合适的位置
    :param array:
    :return:
    """
    if not array:
        return array

    print('\n selection sort')
    minimum_index = None
    array_length = len(array)
    for i in range(array_length - 1):
        print('step %s:' % (i + 1), array)  # 每轮循环后，挑出当前轮最小的元素往最左边靠齐
        minimum_index = i
        for j in range(i+1, array_length):  # 找出每个子轮循环里最小的那个元素
            if array[j] < array[minimum_index]:
                minimum_index = j
        if array[minimum_index] < array[i]:  # swap
            array[i], array[minimum_index] = array[minimum_index], array[i]


def insertion_sort(array):  # O(n^2),和前面一样
    """插入排序: 每次将新元素在已排好序的元素中找到它自己大小的合适的位置，并将期插入到该位置中
    原理是将左边的元素构成的有序数组与新元素相比，如果新元素 > 左边所有元素就和左边所有元素比较后，找到合适的位置插入进去
    :param array:
    :return:
    """
    print('\n selection sort')
    length = len(array)
    for i in range(1, length):
        print('step %s:' % (i + 1), array)  # 每轮循环后，把当前元素（新元素)插入到属于它自己的位置上
        current_element = array[i]  # 先保存着当前新插入元素的值，因为转移过程中可能会被覆盖
        current_index = i  # 找到新插入元素值的合适位置，使得前边数组有序 [0, i]，与左边所有元素对比大小，并找到属于自己合适的位置
        while current_index > 0 and current_element < array[current_index-1]:  # 当前元素 < 上一个元素
            array[current_index] = array[current_index - 1]  # 将当前元素赋值为上一个元素（更大的值)
            current_index -= 1  # 将当前元素值 -1，继续与上上个元素比 current_index --
        array[current_index] = current_element  # 重新恢复当前元素的值


def test__sort():
    array = list(range(10))  # Python3 返回的是迭代器，所以都用 list 强转 （Python2 返回的直接就是list）
    random.shuffle(array)  # 随机打乱数组的顺序
    sorted_array = sorted(array)

    bubble_sort(array)
    assert array == sorted_array

    array = list(range(10))
    random.shuffle(array)
    sorted_array = sorted(array)
    selection_sort(array)
    assert array == sorted_array

    array = list(range(10))
    random.shuffle(array)
    sorted_array = sorted(array)
    insertion_sort(array)
    assert array == sorted_array


if __name__ == '__main__':
    test__sort()
