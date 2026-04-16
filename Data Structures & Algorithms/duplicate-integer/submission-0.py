class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = Counter(nums)
        for i , j in d.items():
            if j > 1:
                return True
        return False