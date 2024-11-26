
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_length = 0
        for i in reversed(s):
            if i == ' ':
                if word_length > 0:
                    break
            else:
                word_length += 1
        return word_length
    
s = "fly me to the moon  "
print(Solution().lengthOfLastWord(s))