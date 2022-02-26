class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    matrix[:] = [list(el)[::-1] for el in zip(*matrix)]
    matrix[:] = zip(*matrix[::-1])