class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    dic = {}
    answer = []
    for str in strs:
      temp = "".join(sorted(str)) 
      if temp in dic:
        dic[temp].append(str) 
      else:
        dic[temp] = [str]
    for _, v in dic.items():
      answer.append(v)
    return answer