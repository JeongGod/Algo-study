//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/01/26.
// Programmers > 스택/큐 > 프린터

import Foundation

func solution(_ priorities: [Int], _ location: Int) -> Int {

    // (index , priority)
    var queue: [(Int, Int)] = []

    for i in 0..<priorities.count {
        queue.append((i, priorities[i]))
    }

    var printed: [(Int, Int)] = []

    while !queue.isEmpty {
        let (index, priority) = queue.removeFirst()

        if queue.contains(where: { $0.1 > priority }) == true {
            queue.append((index, priority))
        } else {
            printed.append((index, priority))
        }
    }
    
    return printed.firstIndex { $0.0 == location }! + 1
}

// print(solution([2, 1, 3, 2], 2)) // 1
// print(solution([1, 1, 9, 1, 1, 1], 0)) // 5
