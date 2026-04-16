class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        thisset = set(nums)

        for i in nums:
            seq, j = 0, i
            while j in thisset:
                seq += 1
                j += 1
            result = max(result, seq)
        return result