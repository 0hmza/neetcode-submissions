class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        i = 0
        while i < len(nums):
            a , j= nums[i],  i
            nums.pop(i)
            result.append(math.prod(nums))
            nums.insert(j, a)
            i += 1
        return result
            