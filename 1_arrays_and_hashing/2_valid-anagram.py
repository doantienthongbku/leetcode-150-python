# https://leetcode.com/problems/valid-anagram/


from collections import Counter

# Time Complexity: O(n) - beats 91.99% of submissions in Python3
# Space Complexity: O(1) - beats 64.67% of submissions in Python3

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)