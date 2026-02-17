class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_posision = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[insert_posision],nums[i]=nums[i],nums[insert_posision]
                insert_posision +=1
        