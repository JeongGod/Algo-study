//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/03/30.
//  Programmers > 스택/큐 > 기능개발

import Foundation

func solution(_ progresses: [Int], _ speeds: [Int]) -> [Int] {

    var answer: [Int] = []
    var newProgresses = progresses
    var newSpeeds = speeds

    while !newProgresses.isEmpty {

        let length = newProgresses.count

        for j in 0..<length {
            newProgresses[j] += newSpeeds[j]
        }

        var counter = 0
        while true {
            guard let firstElement = newProgresses.first else { break }
            if firstElement >= 100 {

                newProgresses.removeFirst()
                newSpeeds.removeFirst()
                counter += 1
            } else {
                break
            }
        }

        if counter > 0 { answer.append(counter) }

    }
    return answer
}

//print(solution([93, 30, 55], [1, 30, 5]))
//print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
