class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible =0
        noneDivisible =0
        for num in range(1,n+1):
            if num % m ==0:
                divisible +=num
            else:
                noneDivisible +=num
        return noneDivisible - divisible
