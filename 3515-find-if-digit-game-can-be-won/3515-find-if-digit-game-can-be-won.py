class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        oneDigit =0
        moredigit = 0
        for x in nums :
            if x <10:
                oneDigit+=x
            else:
                moredigit +=x
        if oneDigit  != moredigit:
            return True
        else:
            return False