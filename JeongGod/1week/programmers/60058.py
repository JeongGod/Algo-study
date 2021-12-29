def solution(p):
    if p == "":
        return ""
    cnt = 0
    u, v = "", ""

    # u, v 분리
    for idx in range(len(p)):
        if p[idx] == "(":
            cnt += 1
        else:
            cnt -= 1
        # 균형잡힌 괄호 문자열
        if cnt == 0:
            u = p[: idx + 1]
            v = p[idx + 1 :]
            break

    # 올바른 괄호인지 check
    def check(brackets):
        st = []
        for bracket in brackets:
            if bracket == "(":
                st.append(bracket)
            else:
                if len(st) == 0:
                    return False
                st.pop()

        if len(st) != 0:
            return False
        return True

    if check(u):
        return u + solution(v)
    else:
        u = u[1:-1]
        table = u.maketrans("()", ")(")
        return "(" + solution(v) + ")" + u.translate(table)
