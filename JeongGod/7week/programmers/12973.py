def solution(s):
    answer = -1
    st = []
    
    for i in s:
        if not st:
            st.append(i)
            continue
        if i == st[-1]:
            st.pop()
        else:
            st.append(i)
    
    # 스택이 비어있다면 참, 아니라면 거짓
    return 1 if not st else 0
