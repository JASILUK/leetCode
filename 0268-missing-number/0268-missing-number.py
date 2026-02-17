class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        totalsum = n*(n+1)//2
        current_sum = sum(nums)
        missed = totalsum - current_sum
        return missed
        