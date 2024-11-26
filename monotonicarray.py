class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if not nums:
             return True
        increasing=True
        decreasing=True
        for i in range(1, len(nums)):
             if nums[i] > nums[i - 1]:
                  decreasing=False
             if nums[i] <nums[i-1]:
                  increasing=False
        return increasing or decreasing
    


                  







Solution=Solution()

nums = [1,3,2]
print(Solution.isMonotonic(nums))