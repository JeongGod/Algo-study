class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dic = {}

        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str in anagram_dic:
                anagram_dic[sorted_str].append(str)
            else:
                anagram_dic[sorted_str] = [str]

        return list(value for key, value in anagram_dic.items())
