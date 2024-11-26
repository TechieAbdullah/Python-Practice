class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count_dict = {}
        for i in nums:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
        most_repeated_element = max(count_dict, key=count_dict.get)
        return most_repeated_element