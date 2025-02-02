## Anagram Leetcode 242
## Given two strings s and t, return true if t is an anagram of s, and false otherwise.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charFreq = [0]*26
        for i in range (len(s)):
            charFreq[ord(s[i]) - ord('a')]+=1 #`ord` function returns the ASCII value of the character
            charFreq[ord(t[i]) - ord('a')]-=1
        for count in charFreq:
            if count:
                return False
           
        return True

# Time complexity: O(n)
# Space complexity: O(1) as the size of the array is fixed
# Approach: Create an array of size 26 and store the frequency of each character in the array. If the frequency of the characters in both the strings is the same, then return True. Else, return False.

## Test cases
s = Solution()
print(s.isAnagram("anagram", "nagaram")) # True
print(s.isAnagram("rat", "car")) # False

