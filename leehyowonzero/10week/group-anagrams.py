class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        anagram_dict = dict()
        strs.sort()
        for el in strs:
            sorted_el = ''.join(sorted(el))
            if(sorted_el not in anagram_dict):
                anagram_dict[sorted_el] = []
                anagram_dict[sorted_el].append(el)
            else:
                anagram_dict[sorted_el].append(el)
        print(anagram_dict)

        for keys in anagram_dict:
            answer.append(anagram_dict[keys])
        return answer