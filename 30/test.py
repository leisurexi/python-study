# author: leisurexi
# date: 2021/1/26
# file name: test.py
# Python 单元测试

import unittest
from unittest.mock import MagicMock


# 将要被测试的排序函数
def sort(arr):
    length = len(arr)
    changed = False
    for i in range(length - 1):
        for j in range(length - i - 1):
            temp = arr[j]
            if temp > arr[j + 1]:
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                changed = True
        # 本次循环没有找到需要交换位置的，代表后续已经不需要排序了
        if not changed:
            break


# 编写子类基础 unittest.TestCase
class TestSort(unittest.TestCase):

    # 以 test 开头的函数将会被测试
    def test_sort(self):
        arr = [3, 4, 1, 5, 6]
        sort(arr)
        # assert 结果跟我们期待的一样
        self.assertEqual(arr, [1, 3, 4, 5, 6])


# mock 的用法
class A(unittest.TestCase):
    def m1(self):
        val = self.m2()
        self.m3(val)

    def m2(self):
        pass

    def m3(self, val):
        pass

    def test_m1(self):
        a = A()
        a.m2 = MagicMock(return_value="custom_val")
        a.m3 = MagicMock()
        a.m1()
        self.assertTrue(a.m2.called)  # 验证 m2 被 call 过
        a.m3.assert_called_with('custom_val')  # 验证 m3 被指定参数 call 过


# Mock Side Effect
def side_effect(arg):
    if arg < 0:
        return 1
    else:
        return 2


if __name__ == '__main__':
    # unittest.main()

    mock = MagicMock()
    mock.side_effect = side_effect
    print(mock(-1))
    print(mock(1))
