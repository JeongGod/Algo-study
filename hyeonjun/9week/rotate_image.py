class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        length = len(matrix)-1
        start_x, start_y = 0, 0
        while length > 0:
            for i in range(length):
                nx = start_x
                ny = start_y+i

                matrix[nx][ny], matrix[ny][nx+length], matrix[nx+length][nx+length-i], matrix[nx+length -
                                                                                              i][nx] = matrix[nx+length-i][nx], matrix[nx][ny], matrix[ny][nx+length], matrix[nx+length][nx+length-i]

            start_x += 1
            start_y += 1
            length -= 2
