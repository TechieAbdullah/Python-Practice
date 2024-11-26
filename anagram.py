
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_map = {}
        
        for char in s:
            if char in count_map:
                count_map[char] += 1
            else:
             count_map[char] = 1
        for char in t:
           if char in count_map:
              count_map[char] -= 1
           else:
              count_map[char] = -1
        return all( count==0
           for count in count_map.values()
        )
solution = Solution()
string1 = 'anagram'
string2 = 'nagaram'
print(solution.isAnagram(string1, string2))
