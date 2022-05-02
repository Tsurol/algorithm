# coding:utf-8
from typing import List
import error_info as ei


class Solution(object):

    def __init__(self):
        pass

    @staticmethod
    def tow_sum_enum(nums: List[int], target: int) -> List[int]:
        """两数之和
        给定一个整数数组 nums 和一个整数目标值 target，
        请你在该数组中找出和为目标值 target的那两个整数，
        并返回它们的数组下标。

        输入：nums = [3,2,4], target = 6
        输出：[1,2]

        tips:
        你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
        你可以按任意顺序返回答案。
        """
        # 暴力枚举出所有组合，时间复杂度为O(N^2)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        raise ei.TipException('No two sum solution')

    @staticmethod
    def two_sum_hash(nums: List[int], target: int) -> List[int]:
        # 查找表法，时间复杂度为O(N)
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i
        raise ei.TipException('No two sum solution')
