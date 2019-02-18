# coding:utf-8
# @Time : 2019/2/18 18:11 
# @Author : Andy.Zhang
# @Desc : 创建集合 set (继承前面的hash_table)


import sys
sys.path.append('../07_hash')
from hash_table import HashTable


# ######################################################
# # 下边是实现 set 抽象数据类型，继承了之前的 hash_table
# ######################################################
class SetADT(HashTable):
    def add(self, key):
        return super(SetADT, self).add(key, True)

    def __and__(self, other_set):
        """交集 A&B"""
        new_set = SetADT()
        for element_a in self:
            if element_a in other_set:
                new_set.add(element_a)
        return new_set

    def __sub__(self, other_set):
        """差集 A-B"""
        new_set = SetADT()
        for element_a in self:
            if element_a not in other_set:
                new_set.add(element_a)
        return new_set

    def __or__(self, other_set):
        """并集 A|B"""
        new_set = SetADT()
        for element_a in self:
            new_set.add(element_a)
        for element_b in other_set:
            new_set.add(element_b)
        return new_set


def test_set_adt():
    sa = SetADT()
    sa.add(1)
    sa.add(2)
    sa.add(3)
    assert 1 in sa

    sb = SetADT()
    sb.add(3)
    sb.add(4)
    sb.add(5)

    assert sorted(list(sa & sb)) == [3]
    assert sorted(list(sa - sb)) == [1, 2]
    assert sorted(list(sa | sb)) == [1, 2, 3, 4, 5]
