class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}

        for n in nums:
            count[n] = count.get(n,0)+1
        for key , value in count.items():
            if value > len(nums)// 2:
                return key