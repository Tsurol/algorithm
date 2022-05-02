# coding:utf-8
import copy
from typing import List
import error_info as ei


class Solution(object):

    def __init__(self):
        pass

    @staticmethod
    def tow_sum_enum(nums: List[int], target: int) -> List[int]:
        """两数之和 暴力枚举法，时间复杂度为O(N^2)"""
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        raise ei.TipException('No two sum solution')

    @staticmethod
    def two_sum_hash(nums: List[int], target: int) -> List[int]:
        """两数之和 查找表法，时间复杂度为O(N)"""
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i
        raise ei.TipException('No two sum solution')

    @staticmethod
    def is_palindrome(x: int) -> bool:
        """回文数"""
        return str(x) == str(x)[::-1]
