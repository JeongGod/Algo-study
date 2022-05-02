//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/04/26.
//  Programmers > 위클리 챌린지 > 전력망을 둘로 나누기

import Foundation

func solution(_ n: Int, _ wires: [[Int]]) -> Int {

    var network: [Int: [Int]] = [:]

    for wire in wires {
        network[wire[0], default: []].append(wire[1])
        network[wire[1], default: []].append(wire[0])
    }

    var visited: [Bool] = Array(repeating: false, count: n + 1)
    
    func bfs(_ start: Int) -> Int {
        var bfsQueue: [Int] = [start]
        
        var idx = 0
        
        while idx < bfsQueue.count {
            let poped = bfsQueue[idx]
            idx += 1
            visited[poped] = true
            
            for number in network[poped]! {
                if !visited[number] {
                    bfsQueue.append(number)
                }
            }
        }
        
        return idx
    }
    
    visited[1] = true
    let count = bfs(2)
    var answer = abs(count-(n-count))
    
    for i in 1...n {
        visited = Array(repeating: false, count: n + 1)
        visited[i] = true
        let count = bfs(1)
        answer = min(answer, abs(count-(n-count)))
    }
    
    return answer
}


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
