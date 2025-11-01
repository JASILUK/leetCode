class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = [char for  char in set(sentence) if char.isalpha()]
        if len(alphabets) == 26:
            return True
        else:
            return False
        
