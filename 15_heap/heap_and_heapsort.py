# coding:utf-8
# @Time : 2019/2/23 12:52 
# @Author : Andy.Zhang
# @Desc : 堆与堆排序


import sys
sys.path.append('../02_array_and_list_line_structure')
from array_and_list import Array


#####################################################
# 基于之前实现的 Array 实现 heap
#####################################################
class MaxHeap(object):
    """
    Heaps:
    完全二叉树，最大堆的非叶子节点的值比孩子大，最小堆的非叶子结点值都比孩子小
    Heap包含两个属性，order property 和 shape property(a complete binary tree)，在插入一个新节点的时候，始终保持这两个特性
    插入操作：保持堆发生和完全二叉树属性, sift-up 操作维持属性
    extract操作：只获取根节点数据，并把树最底层最右节点copy到根节点后，sift-down操作维持堆属性

    用数组实现heap，从根节点开始，从上往下从左往右给每个节点编号。根据完全二叉树的性质，给定一个节点i，其父新和孩子的节点编号分别是：
    parent = (i-1) // 2  # // 代表除完以后再取整，相当于：int((i-1) /2)
    left = i*2 + 1
    right = i*2 + 2

    使用数组实现堆一方面效率高，节省树节点的内存占有，另一方面还可以避免复杂的指针操作，减少调试难度
    """

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        """
        添加节点
        :param value:
        :return:
        """
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count-1)  # 维持堆的特性

    def _siftup(self, index):
        """
        将当前index所对应的值与期parent对比，递归交换，直到满足最大堆特性
        :param index: 当前值的索引
        :return: None
        """
        if index > 0:
            parent = int((index-1) / 2)  # get current element's root index
            if self._elements[index] > self._elements[parent]:  # 如果插入的值大于 parent，一直交换，直到 <= 为止
                self._elements[index], self._elements[parent] = self._elements[parent], self._elements[index]
                self._siftup(parent)  # 递归一直交换，以维持堆特性

    def extract(self):
        """
        获取并移除根节点的值(最大值)
        返回 root 值，并把最后一个节点移到 root 位置，然后在期孩子中找到最大的孩子并与之交换位置，一直自上而下递归往下交换，直接不大于期孩子为止
        :return:
        """
        if self._count < 0:
            raise Exception('empty')
        value = self._elements[0]  # 保存 root值
        self._count -= 1
        self._elements[0] = self._elements[self._count]  # 最右下的节点放到 root 后 siftDown
        self._siftdown(0)  # 维持堆特性
        return value

    def _siftdown(self, index):
        left = index * 2 + 1
        right = index * 2 + 2
        # datermine which node contains the larger value
        largest = index
        if (left < self._count and
            self._elements[left] >= self._elements[largest] and
            self._elements[left] >= self._elements[right]):  # 原书这个地方没写，实际上找的未必是largest
            largest = left
        elif right < self._count and self._elements[right] >= self._elements[largest]:
            largest = right

        if largest != index:
            self._elements[index], self._elements[largest] = self._elements[largest], self._elements[index]
            self._siftdown(largest)


def test_max_heap():
    import random
    n = 10
    h = MaxHeap(n)
    for i in range(n):
        h.add(i)
    for i in reversed(range(n)):
        assert i == h.extract()


def heap_sort_reverse(array):
    """
    堆排序，倒序
    :param array:
    :return:
    """
    length = len(array)
    maxheap = MaxHeap(length)
    for i in array:
        maxheap.add(i)
    res = []
    for i in range(length):
        res.append(maxheap.extract())
    return res


def test_heap_sort_reverse():
    import random
    l = list(range(10))
    random.shuffle(l)
    assert heap_sort_reverse(l) == sorted(l, reverse=True)


if __name__ == '__main__':
    test_max_heap()
    test_heap_sort_reverse()