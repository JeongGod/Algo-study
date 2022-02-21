//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/02/17.
//  BOJ 20164 홀수 홀릭 호석

import Foundation

let N = readLine()!.map { String ($0) }

func operation(_ N: [String]) -> (minimumAnswer: Int, maximumAnswer: Int) {
    let odds = N.filter { Int($0)! % 2 == 1 }.count

    var maximumAnswer = 0, minimumAnswer = Int.max

    if N.count == 2 {

        let newN = String(Int(N[0])! + Int(N[1])!).map { String($0) }
        let result = operation(newN)

        maximumAnswer = max(maximumAnswer, result.maximumAnswer)
        minimumAnswer = min(minimumAnswer, result.minimumAnswer)

    } else if N.count > 2 {
        for i in 0..<N.count - 2 {
            for j in i + 1..<N.count - 1 {
                let sum = Int(N[0...i].joined())! + Int(N[i + 1...j].joined())! + Int(N[j + 1...N.count - 1].joined())!
                let newN = String(sum).map { String($0) }
                let result = operation(newN)

                maximumAnswer = max(maximumAnswer, result.maximumAnswer)
                minimumAnswer = min(minimumAnswer, result.minimumAnswer)

            }
        }
    }

    if minimumAnswer == Int.max {
        return (odds, odds + maximumAnswer)
    } else {
        return (odds + minimumAnswer, odds + maximumAnswer)
    }
}

var answer = (0, Int.max)
answer = operation(N)

print(answer.0, answer.1)

