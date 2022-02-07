//
//  trt.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/02/07.
//

import Foundation

func solution(_ board: [[Int]]) -> Int {

    let N = board.count
    let dx = [-1, 0, 0, 1] // 상 좌 우 하
    let dy = [0, -1, 1, 0]
    var answer = Int.max
    var costArray: [[Int]] = board
    var visited: [[Bool]] = Array(repeating: Array(repeating: false, count: N), count: N)

    func bfs(_ x: Int, _ y: Int, _ direction: Int, _ cost: Int) {
        var queue: [(x: Int, y: Int, direction: Int, cost: Int)] = []
        queue.append((x, y, direction, cost))
        visited[x][y] = true

        while !queue.isEmpty {

            let (x, y, direction, cost) = queue.first!
            var nextQueue = queue[1..<queue.count]

            if (x == N - 1) && (y == N - 1) {
                answer = min(answer, cost)
            }

            for i in 0..<4 {

                let nx = x + dx[i]
                let ny = y + dy[i]
                let nextDirection = i
                var nextCost = cost

                if (nx < 0 || nx >= N || ny < 0 || ny >= N) || costArray[nx][ny] == 1 { continue }

                if nextDirection == direction {
                    nextCost += 100
                } else {
                    nextCost += 600
                }
                
                if !visited[nx][ny] || costArray[nx][ny] >= nextCost {
                    visited[nx][ny] = true
                    costArray[nx][ny] = nextCost
                    nextQueue.append((nx,ny,nextDirection,nextCost))
                }
            }
            queue = Array(nextQueue)
        }
    }
    
    bfs(0, 0, 2, 0)
    bfs(0, 0, 3, 0)
    
    return answer
}



//
//print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
//print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))
//print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
//print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]))


print(solution([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 0, 0]
    ]))
