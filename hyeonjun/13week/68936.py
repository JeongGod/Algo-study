def solution(arr):
    answer = [0, 0]

    def check(s_x, s_y, e_x, e_y):
        flag = arr[s_x][s_y]
        half = (e_x-s_x+1)//2

        if s_x == e_x:
            answer[flag] += 1
            return 0

        for i in range(s_x, e_x+1):
            for j in range(s_y, e_y+1):
                if arr[i][j] != flag:
                    check(s_x, s_y, e_x-half, e_y-half)
                    check(s_x, s_y+half, e_x-half, e_y)
                    check(s_x+half, s_y, e_x, e_y-half)
                    check(s_x+half, s_y+half, e_x, e_y)
                    return 0

        answer[flag] += 1
        return 0

    check(0, 0, len(arr)-1, len(arr)-1)
    return answer
