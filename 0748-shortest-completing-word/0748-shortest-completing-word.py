from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
        filtered = [ch.lower() for ch in licensePlate if ch.isalpha()]
        
        required = Counter(filtered)
        
        result = None
        
        for word in words:
            word_count = Counter(word)
            
            if all(word_count[c] >= required[c] for c in required):
                
                if result is None or len(word) < len(result):
                    result = word
        
        return result
