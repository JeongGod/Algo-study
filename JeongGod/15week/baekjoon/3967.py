import sys

input = sys.stdin.readline

arr = [0] * 12
visited = [False] * 13

check_seq = {
    5 : [[1, 2, 3, 4]],
    8 : [[0, 2, 5, 7]],
    11 : [[0, 3, 6, 10], [7, 8, 9, 10]],
    12 : [[1, 5, 8, 11], [4, 6, 9, 11]],
}
answer = False

def check(seq : list[list[int, int, int, int]]):
    for s in seq:
        result = 0
        for idx in s:
            result += arr[idx]
        if result != 26:
            return False
    return True


def dfs(cur_idx):
    global answer
    
    # 끝까지 다 채웠을 경우
    if cur_idx == 5 or cur_idx == 8 or cur_idx == 11 or cur_idx == 12:
        # 만약 매직스타가 가능하다면
        if not check(check_seq[cur_idx]):
            return
        if cur_idx == 12:
            answer = True
            return
    # 채워져있는 경우는 패스한다.
    if arr[cur_idx]:
        dfs(cur_idx + 1)

    else:
        # 가능한 숫자를 찾는다.
        for val in range(1, 13):
            if visited[val]:
                continue
            visited[val] = True
            arr[cur_idx] = val
            dfs(cur_idx + 1)
            if answer:
                return
            arr[cur_idx] = 0
            visited[val] = False
            # 가능한 매직스타가 나왔으면 더 볼 필요가 없다.



if __name__ == "__main__":
    idx = 0
    board = []
    for _ in range(5):
        line = input().rstrip()
        board.append(list(line))
        for i in line:
            if i == ".":
                continue
            # 일부 채워진 곳을 방문처리 해놓는다.
            if i != "x":
                val = ord(i) - ord("A") + 1
                visited[val] = True
                arr[idx] = val
            idx += 1

    dfs(0)
    a = 0
    for i in board:
        for idx in range(len(i)):
            if i[idx] != ".":
                i[idx] = chr(arr[a] + ord("A") - 1)
                a += 1
        print("".join(i))
