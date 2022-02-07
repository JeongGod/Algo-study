//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/02/02.
//

import Foundation

func solution(_ orders: [String], _ course: [Int]) -> [String] {

    var counter: [[String]: Int] = [:]
    var answer: [String] = []

    orders.forEach {
        let combinations = makeCombination($0, course)
        for arr in combinations {
            // 값이 있으면 +1, 없으면 1로 딕셔너리 value 세팅
            counter[arr] = counter[arr] == nil ? 1 : counter[arr]! + 1
        }
    }

    counter = counter.filter { $0.value >= 2 }

    for num in course {
        let dict = counter.filter { $0.key.count == num }
        for (key, value) in dict {
            if value == dict.max(by: { $0.value <= $1.value })?.value {
                answer.append(key.joined(separator: ""))
            }
        }
    }
    return answer.sorted()
}

func makeCombination(_ word: String, _ order: [Int]) -> [[String]] {

    let characters = word.map { String($0) }.sorted()
    var result: [[String]] = []

    order.forEach {
        result += combination(characters, $0)
    }

    return result
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

//print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))




