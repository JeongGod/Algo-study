//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/02/16.
//  프로그래머스 > Summer/Winter Coding (~2018) > 영어 끝말잇기 12981

import Foundation

func solution(_ n: Int, _ words: [String]) -> [Int] {

    var usedWords: [String] = []
    
    var answer: [Int] = [0, 0]
    // [가장먼저 탈락하는 사람의 번호, 자신의 탈락하는 턴]

    for (index, word) in words.enumerated() {

        // 첫번째사람
        if index == 0 {
            usedWords.append(word)
        } else if !usedWords.contains(word) && (usedWords.last!.last! == word.first!) {
            usedWords.append(word)
        } else { // 실패한 경우
            answer[0] = (index) % n + 1
            answer[1] = (index) / n + 1
            break
        }
    }

    return answer
}

//print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
//print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
//print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
