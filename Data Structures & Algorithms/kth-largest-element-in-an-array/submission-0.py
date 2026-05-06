class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        p = sorted(nums)
        return p[len(p) - k]