# Group Anagram Leeetcode 49
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        new_arr = []
        # Sort each string and store it in a new array
        for i in range(len(strs)):
            new_arr.append(sorted(strs[i]))
        for i in range(len(new_arr)):
            new_arr[i] = "".join(new_arr[i]) 
            
        # Create a hashmap to store the sorted string as key and the original string as value
        hashmap = {}
        for i in range(len(new_arr)):
            if new_arr[i] in hashmap:
                hashmap[new_arr[i]].append(strs[i]) # If the sorted string is already present in the hashmap, append the original string to the value
            else:
                hashmap[new_arr[i]] = [strs[i]] # Store the sorted string as key and the original string as value in the hashmap
        result = []
        for key in hashmap:
            result.append(hashmap[key]) # Append the values of the hashmap to the result array
        return result
    
# Time complexity: O(n*mlogm) where n is the number of strings and m is the length of the longest string
# Space complexity: O(n)
# Approach: Sort each string and store it in a new array. Create a hashmap to store the sorted string as key and the original string as value.
#           Finally, append the values of the hashmap to the result array and return the result array.

## Test cases
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # [["eat","tea","ate"],["tan","nat"],["bat"]]
print(s.groupAnagrams(["a"])) # [["a"]]
print(s.groupAnagrams([""])) # [[""]]
print(s.groupAnagrams(["abc","def","ghi"])) # [["abc"],["def"],["ghi"]]