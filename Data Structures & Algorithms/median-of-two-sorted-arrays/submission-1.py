class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        thislist = []
        for i in nums1:
            thislist.append(i)
        for i in nums2:
            thislist.append(i)
        p = sorted(thislist)
        if len(p) % 2 != 0:
            result = p[len(p)//2]
        elif len(p) % 2 == 0:
            result = (p[(len(p) // 2)] + p[(len(p) // 2) - 1]) / 2
        return float(result)