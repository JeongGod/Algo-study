from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(sp : int, pp : int):
            if sp == len(s) and pp == len(p):
                return True
            elif sp == len(s) and pp < len(p):
                return dfs(sp, pp+1) and p[pp] == "*"
            elif sp < len(s) and pp == len(p):
                return False
            elif p[pp] == "*":
                return dfs(sp+1, pp) or dfs(sp, pp+1)
            elif s[sp] == p[pp] or (p[pp] == "?" and s[sp] != " "):
                return dfs(sp+1, pp+1)
            return False
        return dfs(0, 0)

