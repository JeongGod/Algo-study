from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        for anagram in strs:
            answer["".join(sorted(anagram))].append(anagram)
        
        return answer.values()

