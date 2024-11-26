
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        empty = set()
        for i in nums:
            if i in empty:
                return True
            empty.add(i)
        return False
nums = [1,2,3,1]
abc = Solution()
print(abc.containsDuplicate(nums))