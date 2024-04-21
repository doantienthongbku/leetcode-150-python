# https://leetcode.com/problems/two-sum/

from typing import List

# Time Complexity: O(n) - beats 70.42% of submissions in Python3
# Space Complexity: O(n) - beats 60.2% of submissions in Python3

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            if (target - nums[i]) in hashmap.keys():
                return [i, hashmap[target - nums[i]]]
            hashmap[nums[i]] = i
            