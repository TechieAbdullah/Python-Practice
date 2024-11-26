from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        pairs = 0
        for num in nums:
            if num in count:
                pairs += count[num]
                count[num] += 1
            else:
                count[num] = 1
        return pairs

solution = Solution()

nums1 = [1, 2, 3, 1, 1, 3]
print("Input: nums =", nums1)
print("Output:", solution.numIdenticalPairs(nums1))
print("Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.\n")

nums2 = [1, 1, 1, 1]
print("Input: nums =", nums2)
print("Output:", solution.numIdenticalPairs(nums2))
print("Explanation: Each pair in the array are good.\n")

nums3 = [1, 2, 3]
print("Input: nums =", nums3)
print("Output:", solution.numIdenticalPairs(nums3))
print("Explanation: There are no good pairs.\n")