//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/01/18.
//

import Foundation

func solution(_ begin: String, _ target: String, _ words: [String]) -> Int {

    if !words.contains(target) {
        return 0
    } else {
        let newWords: [String] = [begin] + words
        var visited: [Int] = Array(repeating: 0, count: newWords.count)
        var que: [(word: String, move: Int)] = []

        que.append((begin, 0)) // 큐에 시작하는 단어와 이동횟수를 담는다.

        while !que.isEmpty {
            let (currentWord, currentMoveCount) = que.removeFirst()
            visited[newWords.firstIndex(of: currentWord)!] = 1
            if currentWord == target { return currentMoveCount }

            for i in 0..<newWords.count {
                if currentWord == newWords[i] { continue }
                if visited[newWords.firstIndex(of: newWords[i])!] == 1 { continue }
                if isDifferentOneCharacter(newWords[i], currentWord) {
                que.append((newWords[i], currentMoveCount + 1))
                visited[newWords.firstIndex(of: currentWord)!] = 1
                }
                
            }
        }
        return 0
    }
}


// 한번에 한개의 알파벳만 바꿀 수 있기 때문에 두 단어가 한개의 알파벳만 다른지 확인하는 함수

func isDifferentOneCharacter(_ a: String, _ b: String) -> Bool {
    var wrongCount: Int = 0
    for i in 0..<a.count {
        if a[a.index(a.startIndex, offsetBy: i)] != b[b.index(b.startIndex, offsetBy: i)] {
            wrongCount += 1
        }
        if wrongCount > 1 { return false }
    }
    return true
}


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
