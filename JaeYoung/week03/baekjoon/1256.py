from math import factorial


def getFactorial(a, b) -> int:
    return (factorial(a+b)) / (factorial(a) * factorial(b))


def main(N, M, K) -> str:
    answer = ""
    W = 0  # 누적 경우의 수
    P = 0  # 남은 문자열로 만들 수 있는 문자열 경우의 수

    while True:
        if N != 0:
            N -= 1
            answer += "a"
            P = getFactorial(N, M)
            T = W + P  # 해당 문자열까지 포함된 경우의 수

            # 문자열을 만들 수 있는 경우의 수가 하나뿐이고 해당 문자열까지 포함된 경우의 수가 K랑 같으면
            # 해당 문자열을 만들 수 있는 경우가 정답
            if P == 1 and T == K:
                answer += N*"a" + M*"z"  # 남아있는 a문자 or z문자 추가
                break

            # 문자열을 만들 수 있는 해당 문자열까지 포함된 경우의 수가 K 보다 작으면 문자열 추가를 위해 continue
            if K <= T:
                continue

            # 문자열을 만들 수 있는 해당 문자열까지 포함된 경우의 수가 K 보다 크면
            # a문자를 빼고 z 문자로 대체
            # 누적 경우의 수 W = T 로 변경
            elif K > T:
                W = T
                answer = answer[:-1]
                answer += "z"
                N += 1
                M -= 1

    return answer


if __name__ == "__main__":
    N, M, K = map(int, input().split())

    # 사전에 수록되어 있는 문자열의 개수가 K보다 작으면 -1을 출력
    if getFactorial(N, M) < K:
        print("-1")

    else:
        print(main(N, M, K))