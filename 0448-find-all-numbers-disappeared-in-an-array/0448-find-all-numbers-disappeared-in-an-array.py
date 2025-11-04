class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        new = set (range(1,len(nums)+1))
        seted = set(nums)
        return list(new - seted)