# Top K Frequent Elements 
# Given a non-empty array of integers, return the k most frequent elements.
import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if k == len(nums):
            return list(set(nums)) 
        # Create a hashmap to store the frequency of each element in the array
        freq_map = {}
        for n in nums: 
            freq_map[n] = freq_map.get(n, 0) + 1 # Store the frequency of each element in the array
        heap = []
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))  # Push the element and its frequency to the heap
            if len(heap) > k:
                heapq.heappop(heap)  # Pop the element with the minimum frequency if the length of the heap exceeds k

        return [num for freq, num in heap] # Return the elements in the heap
    
# Time complexity: O(nlogk) where n is the number of elements in the array and k is the number of most frequent elements to return
# Space complexity: O(n)

# Approach: Create a hashmap to store the frequency of each element in the array. Create a min heap to store the elements based on their frequency.
#           For each element in the hashmap, push the element and its frequency to the heap. If the length of the heap exceeds k, pop the element with the minimum frequency.
#           Finally, return the elements in the heap.

# Test cases
s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2)) # [1,2]
print(s.topKFrequent([1], 1)) # [1]
print(s.topKFrequent([1,2,3,4,5], 3)) # [3,2,1]
print(s.topKFrequent([1,2,3,4,5], 5)) # [1,2,3,4,5]

