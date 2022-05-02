//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/05/01.
//  BOJ > 2623 > 음악프로그램

import Foundation

var N = 0, M = 0
var edges = Array(repeating: Array(repeating: false, count: 1001), count: 1001)
var indegree = Array(repeating: 0, count: 1001)

struct Queue {
    var queue = [Int]()
    var front = 0

    var isEmpty: Bool {
        return front >= queue.count
    }

    mutating func insert(_ n: Int) {
        queue.append(n)
    }

    mutating func popFirst() -> Int {
        let result = queue[front]
        front += 1
        return result
    }
}

func topologySort() -> [Int] {
    var result: [Int] = []
    var queue = Queue()

    for i in 1...N {
        if indegree[i] == 0 {
            queue.insert(i)
        }
    }

    while !queue.isEmpty {
        let current = queue.popFirst()

        result.append(current)

        for end in 1...N {
            if edges[current][end] {
                indegree[end] -= 1
                if indegree[end] == 0 { queue.insert(end) }
            }
        }
    }

    if result.count != N { return [0] }
    else { return result }
}

var input = readLine()!.split(separator: " ").map { Int($0)! }
N = input[0]
M = input[1]

for _ in 0..<M {
    input = readLine()!.split(separator: " ").map { Int($0)! }
    for i in 1..<input.count - 1 {
        let start = input[i]
        let end = input[i + 1]

        if !edges[start][end] {
            edges[start][end] = true
            indegree[end] += 1
        }
    }
}

let result = topologySort()
print(result)
result.forEach { print($0) }

