# https://leetcode.com/problems/contains-duplicate

from typing import List


# Time Complexity: O(n) - beats 75.3% of submissions in Python3
# Space Complexity: O(n) - beats 65.45% of submissions in Python3

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
