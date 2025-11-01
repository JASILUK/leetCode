class Solution:
    def countDigits(self, num: int) -> int:
        result =0
        for x in str(num):
            if num % int(x) ==0:
                result +=1
        return result