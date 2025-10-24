class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        removearr = []
        while val in nums:
            nums.remove(val)
            removearr.append('_')
        result = sorted(nums).extend(removearr)
        return result