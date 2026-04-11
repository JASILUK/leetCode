class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        result =""
        check = ""
        for char in pre:
            check +=char
            for num in strs:
                if not num.startswith(check):
                    return result
                    break
            else:
                result +=char
                
        return result

            