class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [sorted([(i, j) for i, j in Counter(nums).items()], key=lambda x: x[1], reverse=True)[i][0] for i in range(0, k)]
