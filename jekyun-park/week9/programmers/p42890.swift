//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/02/23.
//  Programmers > 2019 KAKAO BLIND RECRUITMENT > 후보키

import Foundation

func isUnique(_ relation: [[String]], _ columns: [Int]) -> Bool {
    var uniqueColumns: Set<String> = []

    for tuple in relation {
        var tupleString = ""

        for column in columns {
            tupleString += tuple[column]
        }

        if uniqueColumns.contains(tupleString) { return false }
        uniqueColumns.update(with: tupleString)
    }

    return true
}

func isMinimal(_ relation:[[String]], _ key:[Int]) -> Bool {
    
    for i in 1..<key.count {
        var candidates: [[Int]] = []
        
        candidates = combination(key, i)
        
        for candidate in candidates {
            if isUnique(relation, candidate) {
                return false
            }
        }
    }
    
    return true
}

func solution(_ relation: [[String]]) -> Int {

    var answer: Int = 0
    var candidates: [[Int]] = []

    // 모든 조합을 구한다.
    for i in 1...relation[0].count {
        candidates = combination(Array(0..<relation[0].count), i)

        for candidate in candidates {
            if isUnique(relation, candidate) && isMinimal(relation, candidate) {
                answer += 1
            }
        }

    }
    
    return answer
}

func combination<T>(_ elements: [T], _ k: Int) -> [[T]] {
    var result = [[T]]()

    func combi(_ index: Int, _ now: [T]) {
        if now.count == k {
            result.append(now)
            return
        }
        for i in index..<elements.count {
            combi(i + 1, now + [elements[i]])
        }
    }
    combi(0, [])
    return result
}

print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
