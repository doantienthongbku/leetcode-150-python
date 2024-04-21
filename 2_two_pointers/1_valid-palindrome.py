# https://leetcode.com/problems/valid-palindrome


# Time Complexity: O(n) - beats 73.49% of submissions in Python3
# Space Complexity: O(1) - beats 47.05% of submissions in Python3

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1

        while left < right:
            while (not s[left].isalnum()) and (left < right): left += 1
            while (not s[right].isalnum()) and (left < right): right -= 1
            if (s[left] != s[right]): return False
            left += 1
            right -= 1
        
        return True