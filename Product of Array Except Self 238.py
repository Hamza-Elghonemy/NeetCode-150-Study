# Product of Array Except Self - Medium
# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        post = 1
        pre = 1
        size = len(nums)
        result = [1]*size
        for i in range (size):
            result[i] = pre  # result[i] stores the product of all the elements to the left of i
            pre = pre*nums[i] # update pre variable 
        for i in range (size -1,-1,-1):  # loop from right to left 
            result[i] = result[i] * post 
            post = post * nums[i]
        return result
    
# Time complexity: O(n)
# Space complexity: O(1) as the size of the array is fixed


# Test cases
s = Solution()
print(s.productExceptSelf([1,2,3,4])) # [24,12,8,6]
print(s.productExceptSelf([-1,1,0,-3,3])) # [0,0,9,0,0]
print(s.productExceptSelf([1,2,3,4,5,6])) # [720,360,240,180,144,120]

