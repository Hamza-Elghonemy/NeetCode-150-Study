## Contains Duplicate Leetcode 217
## Given an array of integers, find if the array contains any duplicates.
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        duplicate = False
        hs = set()
        for i in range(len(nums)):
            if nums[i] in hs:
                duplicate = True
                break
            else:
                hs.add(nums[i])

        return duplicate
            

## Time Complexity: O(n)
## Space Complexity: O(n)

## Test cases
s = Solution()
print(s.containsDuplicate([1,2,3,1])) # True
print(s.containsDuplicate([1,2,3,4])) # False