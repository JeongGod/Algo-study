import sys

input = sys.stdin.readline

def check(bit : int, networks : int) -> bool:
    for val in networks:
        if networks[0] & bit != val & bit:
            return False
    return True

def solution(networks : list[int]) -> None:
    m = 0
    for i in range(31, -1, -1):
        bit = 1 << i
        if not check(bit, networks):
            m = i+1
            break
    mask = 0
    for i in range(32-m):
        mask |= (1 << i)
    for _ in range(m):
        mask <<= 1
    
    ans = mask & networks[0]
    print(f"{(ans >> 24)& 255}.{(ans >> 16)& 255}.{(ans >> 8)& 255}.{ans & 255}")
    print(f"{(mask >> 24)& 255}.{(mask >> 16)& 255}.{(mask >> 8)& 255}.{mask & 255}")
    

def net_to_bit(x : list[str, str, str, str]) -> int:
    result = 0
    for i in map(int, x):
        result <<= 8
        result |= i
    return result

if __name__ == "__main__":
    N = int(input())
    networks = [net_to_bit(input().rstrip().split(".")) for _ in range(N)]
    solution(networks)
