def solution(s):
    answer = 0
    open_s = {"[" : 0, "{" : 1, "(" : 2}
    close_s = {"]" : 0, "}" : 1, ")" : 2}
    st = []
    
    def check(shift_s):
        for ss in shift_s:
            if ss in open_s:
                st.append(ss)
            else:
                if len(st) == 0:
                    return False
                if open_s[st[-1]] == close_s[ss]:
                    st.pop()
                else:
                    return False
        if len(st) != 0:
            return False
        return True

    def rotate(s):
        tmp = s[0]
        result = ""
        for i in range(len(s)-1):
            result += s[i+1]
        result += tmp
        return result
        
    for _ in range(len(s)):
        if check(s):
            answer +=1
        s = rotate(s)
        
    
    return answer