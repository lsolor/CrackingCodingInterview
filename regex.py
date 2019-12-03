class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        tp = p
        p = ""
        for c in range(len(tp)):
            if c > 0 and tp[c] == '*' and tp[c - 1] == '*':
                pass
            else:
                p += tp[c]
        mem = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        if len(s) < len(p) - p.count('*'):
            return False

        mem[0][0] = True
        if len(p) > 0 and p[0] == '*':
            mem[0][1] = True
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    mem[i][j] = mem[i - 1][j - 1]
                elif p[j - 1] == '*':
                    mem[i][j] = mem[i - 1][j] or mem[i][j - 1]
        print(mem)
        return mem[len(s)][len(p)]
