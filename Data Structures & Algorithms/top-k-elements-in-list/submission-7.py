class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        p = sorted([(i, j) for i, j in Counter(nums).items()], key=lambda x: x[1], reverse=True)
        thislist = []
        for i in range(0, k):
            thislist.append(p[i][0])
        return thislist