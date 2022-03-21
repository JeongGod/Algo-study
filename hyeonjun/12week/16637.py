import sys
input = sys.stdin.readline

if __name__ == '__main__':

    def cut(idx, res, sym):
        global ans
        if idx >= N:
            ans = max(ans, int(res))
            return 0

        tmp = '+'
        if idx+3 < N:
            tmp = exp[idx+3]
        cut(idx+4, str(eval(res+sym + str(eval(exp[idx:idx+3])))), tmp)
        cut(idx+2, str(eval(res+sym+exp[idx])), exp[idx+1])

    ans = float('-inf')
    N = int(input())
    exp = input()
    cut(0, '0', '+')
    print(ans)
