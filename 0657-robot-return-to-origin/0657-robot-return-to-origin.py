class Solution:
    def judgeCircle(self, moves: str) -> bool:
        left =[]
        right = []
        top = []
        down = []
        for char in moves:
            if char =='L':
                left.append(char)
            elif char == 'R':
                right.append(char)
            elif char =='U':
                top.append(char)
            else:
                down.append(char)
        if len(left) == len(right) and len(top) == len(down):
            return True
        else:
            return False