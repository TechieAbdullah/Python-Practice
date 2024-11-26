class Solution:
    def replaceElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n - 1):
            nums[i] = max(nums[i + 1:])
        nums[-1] = -1
        return nums

nums = [17, 18, 5, 4, 6, 1]
solution = Solution()
result = solution.replaceElements(nums)
print(result)