class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        ans = ""
        for i in range(n):
            if i + 2 < n and num[i] == num[i + 1] == num[i + 2]:
                current = num[i:i + 3]
                if current > ans:
                    ans = current
        return ans
num = "6888124999"