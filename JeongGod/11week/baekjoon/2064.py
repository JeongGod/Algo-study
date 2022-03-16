import sys

input = sys.stdin.readline

def solution(n : int, networks : list[list[int, int, int, int]]):
    """
    1. 네트워크 마스크를 먼저 찾는다.
        1. and 연산을 진행한다.
        2. and연산을 한 것을 바탕으로 모든 네트워크와 not(xor)연산을 한다.
        3. not(xor)연산한 것을 and연산을 한다 => 네트워크 마스크
    2. 찾은 네트워크 마스크를 이용해 네트워크 주소중 하나를 선택해 and연산을 한다.
    """
    save = networks[0][:]
    result_and = [0, 0, 0, 0]
    for j in range(4):
        tmp = 255
        for i in range(n):
            tmp &= networks[i][j]
        result_and[j] = tmp
    
    
    for j in range(4):
        for i in range(n):
            networks[i][j] = ~(networks[i][j] ^ result_and[j])

    mask = [0, 0, 0, 0]
    for j in range(4):
        tmp = 255
        for i in range(n):
            tmp &= networks[i][j]
        mask[j] = tmp
        if tmp != 255:
            break
    
    ans = [0, 0, 0, 0]
    for j in range(4):
        ans[j] = save[j] & mask[j]
    print(".".join(map(str, ans)))
    print(".".join(map(str, mask)))

if __name__ == "__main__":
    N = int(input())
    networks = [list(map(int, input().rstrip().split("."))) for _ in range(N)]
    solution(N, networks)
