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

    @staticmethod
    def roman_to_int(s: str) -> int:
        """罗马数字转整数"""
        symbol_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        answer = 0
        n = len(s)
        for i, v in enumerate(s):
            value = symbol_values[v]
            if i < n - 1 and value < symbol_values[s[i + 1]]:
                answer -= value
            else:
                answer += value
        return answer

    @staticmethod
    def longest_common_prefix(strs: List[str]) -> str:
        """最长公共前缀"""
        result = ""
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                result += tmp[0]
            else:
                break
        return result
