from typing import List


def solution(s: str):
    stack:List[str] = []
    stack.append(s[0])
    
    for i in range(1, len(s)):
        if not stack:
            stack.append(s[i])
            continue
        
        if stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
        
    if stack:
        return 0
    else:
        return 1

# abbbba
# aabbbb

# print(solution("baabaa"))
# print(solution("cdcd"))