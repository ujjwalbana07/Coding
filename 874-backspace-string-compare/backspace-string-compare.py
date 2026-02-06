class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = []
        b = []

        for i in s:

            if i!= "#":
                a.append(i)
            else:
                if len(a) != 0:
                    a.pop()
            
        for i in t:
            if i!= "#":
                b.append(i)
            else:
                if len(b) != 0:
                    b.pop()
            
        if a == b:
            return True
        else:
            return False
        