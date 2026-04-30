class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for first in range(n-3):
            if first >0 and nums[first] == nums[first-1]:
                continue
            
            for second in range(first+1,n-2):
                if second > first+1 and nums[second] == nums[second-1]:
                    continue

                left = second+1
                right = n-1
                
                while left < right :
                    total = nums[first]+nums[second]+nums[left]+nums[right]

                    if target == total:
                        result.append([nums[first],nums[second],
                                        nums[left],nums[right]])

                        while left <right and nums[left] == nums[left+1]:
                            left +=1
                        while left < right and nums[right] == nums[right-1]:
                            right -=1
                        
                        left +=1
                        right -=1

                    elif total < target :
                        left +=1
                    else :
                        right -=1
        return result