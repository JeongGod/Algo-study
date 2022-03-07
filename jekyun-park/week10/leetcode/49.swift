//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/03/02.
//  LeetCode > 49. Group Anagrams

import Foundation

class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        var answer: [[String]] = []
        var wordDictionary: [[String.Element]: [String]] = [:]

        for word in strs {
            let anagram = Array(word).sorted()
            
            if wordDictionary[anagram] == nil {
                wordDictionary[anagram] = [word]
            } else {
                wordDictionary[anagram]!.append(word)
            }
        }

        wordDictionary.values.forEach { answer.append($0) }
        
        return answer
    }
}

// default:[] 로 defaultDict 사용가능
class Solution2 {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        var wordDictionary: [[String.Element]: [String]] = [:]

        for word in strs {
            let anagram = Array(word).sorted()
            wordDictionary[anagram,default: []].append(word)
        }
        
        return Array(wordDictionary.values)
    }
}

