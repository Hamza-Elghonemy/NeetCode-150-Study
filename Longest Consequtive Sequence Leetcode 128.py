# Longest Consecutive Sequence Leetcode 128
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        hs = set(nums)
        lcs = 1
        for num in hs: # loop through the set
            curcs = 1
            if num-1 in hs: # if the previous element is present in the set --> Cannot be the start of the sequence
                continue
            seq = num + 1 
            while seq in hs: # loop until the next element in sequence is not present in the set
                curcs += 1
                seq += 1
            lcs = max(lcs,curcs) # update the longest consecutive sequence
        return lcs

# Time complexity: O(n)
# Space complexity: O(n)

# Test cases
s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2])) # 4
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # 9
print(s.longestConsecutive([1,2,0,1])) # 3