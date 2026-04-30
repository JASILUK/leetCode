class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0 
        count = 0
        history ={0:1}

        for i  in range(len(nums)):
            current_sum +=nums[i]

            defrence = current_sum - k
            
            if defrence in history:
                count +=history[defrence]

            history[current_sum] = history.get(current_sum,0)+1
        return count