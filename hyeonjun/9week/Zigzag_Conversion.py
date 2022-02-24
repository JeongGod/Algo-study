class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        pattern_arr = [[]for _ in range(numRows)]
        pattern_repetition = len(s)//((numRows-1)*2)
        pattern = ([i for i in range(numRows-1)] +
                   [i for i in range(numRows-1, 0, -1)]) * (pattern_repetition+1)
        pattern = pattern[:len(s)]

        for idx, letter in enumerate(pattern):
            pattern_arr[letter].append(s[idx])

        answer = ''
        for i in pattern_arr:
            answer += ''.join(i)

        return answer
