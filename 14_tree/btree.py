# coding:utf-8
# @Time : 2019/2/21 19:40 
# @Author : Andy.Zhang
# @Desc : 二叉树 btree


from collections import deque
import sys
sys.path.append('../05_stack')
from stack_structure import Stack


class Queue(object):  # 借助内置的 deque 可以迅速实现一个 Queue
    def __init__(self):
        self._items = deque()

    def append(self, value):
        return self._items.append(value)

    def pop(self):
        return self._items.popleft()

    def is_empty(self):
        return len(self._items) == 0


node_list = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]


class BinTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right


class BinTree(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        """通过节点信息构造二叉树
        第1次遍历构造 node 节点
        第2次遍历给 root 和 孩子赋值，通过root, left, right 整体串起来
        最后用 root 初始化这个类并返回一个对象
        :param node_list: {'data': 'A', 'left': None, 'right': None, 'is_root': False}
        :return:
        """
        node_dict = {}
        for node_data in node_list:
            # 构造 node 节点
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)
        for node_data in node_list:
            # 给 root 和 孩子赋值，指明 哪是root，哪是 left节点，哪是 right，整体串起来
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return cls(root)

    def reverse(self, subtree):
        """反转二叉树，即：左右子节点交换
        """
        if subtree is not None:
            subtree.left, subtree.right = subtree.right, subtree.left  # 将左右子树交换
            self.reverse(subtree.left)  # 不断递归调用，以保证将所有子节点也交换
            self.reverse(subtree.right)

    def preorder_traverse(self, subtree):
        """先(根)序遍历: root=>left=>right
        :param subtree:
        :return:
        """
        if subtree is not None:
            yield subtree.data  # 处理根
            yield from self.preorder_traverse(subtree.left)  # 递归处理左子数，yield from 会 yield函数里面的 yield iterable对象
            yield from self.preorder_traverse(subtree.right)  # 递归处理右子树

    def preorder_traverse_use_stack(self, subtree):
        """用栈来实现先序遍历，递归的方式其实是计算机帮实现了栈结构"""
        if subtree:
            s = Stack()
            s.push(subtree)  # 先入栈
            while not s.is_empty():
                top_node = s.pop()  # 出栈
                yield top_node.data  # 输出(栈)值，当然也可以用 print
                if top_node.right:
                    s.push(top_node.right)  # 先进后出
                if top_node.left:
                    s.push(top_node.left)  # 后进先出

    def inorder_traverse(self, subtree):  # for val in inorder_traverse(root): print(val)
        """中(根)序遍历: left=>root=>right"""
        if subtree is not None:
            yield from self.inorder_traverse(subtree.left)
            yield subtree.data
            yield from self.inorder_traverse(subtree.right)

    def posorder_traverse(self, subtree):  # 递归实现
        """后(根)序遍历: left=>right=root"""
        if subtree is not None:
            yield from self.posorder_traverse(subtree.left)
            yield from self.posorder_traverse(subtree.right)
            yield subtree.data

    def layer_traverse_use_list(self, subtree):  # 实现 list 来模拟对列
        """层遍历(每层从左=>到右): depth0 => depth1 => depth2"""
        if subtree:
            cur_nodes = [subtree]
            next_nodes = []
            while cur_nodes or next_nodes:
                for node in cur_nodes:
                    yield node.data
                    if node.left:
                        next_nodes.append(node.left)  # 使用 list模拟对列，先进先出
                    if node.right:
                        next_nodes.append(node.right)  # 后进后出
                cur_nodes = next_nodes  # 交换，以继续遍历下一层
                next_nodes = []

    def layer_traverse_use_queue(self, subtree):  # 使用对列
        """层遍历(每层从左=>到右): depth0 => depth1 => depth2"""
        if subtree:
            q = Queue()
            q.append(subtree)
            while not q.is_empty():
                cur_node = q.pop()
                yield cur_node.data
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)


def test_bin_tree():
    btree = BinTree.build_from(node_list)

    print('先序遍历: root => left => right')
    assert list(btree.preorder_traverse(btree.root)) == ['A', 'B', 'D', 'E', 'H', 'C', 'F', 'G', 'I', 'J']
    assert list(btree.preorder_traverse_use_stack(btree.root)) == ['A', 'B', 'D', 'E', 'H', 'C', 'F', 'G', 'I', 'J']

    print('中序遍历: left => root => right')
    assert list(btree.inorder_traverse(btree.root)) == ['D', 'B', 'H', 'E', 'A', 'F', 'C', 'I', 'G', 'J']

    print('后序遍历: left => right => root')
    assert list(btree.posorder_traverse(btree.root)) == ['D', 'H', 'E', 'B', 'F', 'I', 'J', 'G', 'C', 'A']

    print('用列表实现层遍历: depth0 => depth1 => depth2')
    assert list(btree.layer_traverse_use_list(btree.root)) == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    print('用队列实现层遍历: depth0 => depth1 => depth2')
    assert list(btree.layer_traverse_use_queue(btree.root)) == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    print('反转之后的先序遍历结果: 先left, right = right, left， 然后 root => left => right')
    btree.reverse(btree.root)
    assert list(btree.preorder_traverse(btree.root)) == ['A', 'C', 'G', 'J', 'I', 'F', 'B', 'E', 'H', 'D']


if __name__ == '__main__':
    test_bin_tree()
