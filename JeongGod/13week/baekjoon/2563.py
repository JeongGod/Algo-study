import sys

input = sys.stdin.readline

def solution(papers : list[list[int, int]]) -> int:
    board = [[0] * 101 for _ in range(101)];

    for y, x in papers:
        for i in range(x, x+10):
            for j in range(y, y+10):
                board[i][j] = 1
    


    result = 0
    for b in board:
        result += sum(b)


    return result

if __name__ == "__main__":
    N = int(input())
    papers = [list(map(int, input().split())) for _ in range(N)]
    print(solution(papers))
