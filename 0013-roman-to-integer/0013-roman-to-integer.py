class Solution:
    def romanToInt(self, s: str) -> int:
        Values={
            "I"     :        1,
           "V"     :       5,
           "X"     :      10,
           "L"      :      50,
           "C"      :     100,
           "D"     :      500,
           "M"     :      1000
        }
        total = 0
        for x in range(len(s)):
            if x <len(s)-1 and Values[s[x]] < Values[s[x+1]]:
                total -=Values[s[x]]
            else:
                total +=Values[s[x]]
        return total