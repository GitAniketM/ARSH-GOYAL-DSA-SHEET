class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
                
        nums.clear()
        nums.extend(list(d.keys()))
        return len(nums)