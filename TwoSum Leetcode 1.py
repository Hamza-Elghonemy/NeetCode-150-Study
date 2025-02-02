# Two Sum Leetcode 1
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            remainder = target - nums[i] # Calculate the remainder
            if (remainder in hashmap):
                return [hashmap[remainder], i] # If the remainder is present in the hashmap, return the indices
            hashmap[nums[i]] = i # Store the element and its index in the hashmap if the remainder is not present in the hashmap
    
# Time complexity: O(n)
# Space complexity: O(n)
# Approach: Create a hashmap to store the elements and their indices. For each element in the array, calculate the remainder by subtracting the element from the target.
#           if the remainder is present in the hashmap, return the indices. Else, store the element and its index in the hashmap.

## Test cases
s = Solution()
print(s.twoSum([2,7,11,15], 9)) # [0, 1]
print(s.twoSum([3,2,4], 6)) # [1, 2]
print(s.twoSum([3,3], 6)) # [0, 1]

            
            