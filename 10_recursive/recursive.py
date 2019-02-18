# coding:utf-8
# @Time : 2019/2/18 20:11 
# @Author : Andy.Zhang
# @Desc : 递归 recursive


from collections import deque


def factorial(n):  # n!，求n的阶乘 1 * 2 * 3 * ... * n = ?
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def print_num(n):  # print n, n-1, n-2, ... , 1
    for i in range(1, n+1):
        print(i)


def print_num_recursive(n):  # 用递归的方式代替上面打印
    if n > 0:
        print_num_recursive(n-1)
        print(n)


def print_num_recursive_reverse(n):  # 尾递归，print 1, 2, 3, ..., n-2, n-1, n
    if n > 0:
        print(n)
        print_num_recursive_reverse(n-1)


class Stack(object):  # 使用对列来模拟电脑递归调用的时候，入栈和出栈过程
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.pop()

    def is_empty(self):
        return len(self._deque) == 0


def print_num_use_stack(n):  # 使用栈来打印
    s = Stack()
    while n > 0:  # 不断将参数入栈
        s.push(n)
        n -= 1

    while not s.is_empty():
        print(s.pop())  # 参数弹出（出栈）


def hanoi_move(n, source, destination, intermediate):  # 汉诺塔问题, O(2n^2 -1)
    '''
    https://zh.wikipedia.org/wiki/%E6%B1%89%E8%AF%BA%E5%A1%94
    '''
    if n >= 1:  # 递归出口，只剩下一个盘子的情况下
        hanoi_move(n - 1, source, intermediate, destination)
        print('Move disk[%s]: from %s to %s' % (n, source, destination))
        hanoi_move(n - 1, intermediate, destination, source)


def flatten(rec_list):  # 递归list
    for i in rec_list:
        if isinstance(i, list):
            for i in flatten(i):
                yield i
        else:
            yield i


def test_flatten():
    assert list(flatten([[[1], 2, 3], [1, 2, 3]])) == [1, 2, 3, 1, 2, 3]


if __name__ == '__main__':
    print('call factorial(5)')
    print(factorial(5))

    print('\ncall print_num(5)')
    print_num(5)

    print('\ncall print_num_recursive(5)')
    print_num_recursive(5)

    print('\ncall print_num_recursive_reverse(5)')
    print_num_recursive_reverse(5)

    print('\ncall print_num_use_stack(5)')
    print_num_use_stack(5)

    print('\ncall hanoi_move')
    hanoi_move(3, 'A', 'C', 'B')
