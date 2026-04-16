class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        t = dict()
        res = []
        for i in nums:
            if i not in t:
                t[i] = 1
            else:
                t[i] += 1
        for i in range(k):
            p = max(t, key=t.get)
            res.append(p)
            t.pop(p)
        return res
        
