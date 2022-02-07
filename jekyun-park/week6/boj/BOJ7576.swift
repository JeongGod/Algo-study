//
//  secondTry.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/02/04.
//

import Foundation

let boxSize = readLine()!.split(separator: " ").map { Int($0)! }
let M = boxSize[0]; let N = boxSize[1]
var tomatoBox: [[Int]] = []

for _ in 0..<N {
    tomatoBox.append(readLine()!.split(separator: " ").map { Int($0)! })
}

var queue: [(Int, Int)] = []
var distance: [[Int]] = Array(repeating: Array(repeating: 0, count: M), count: N)

for i in 0..<N {
    for j in 0..<M {
        if tomatoBox[i][j] == 1 {
            // 익은 토마토 큐에 삽입
            queue.append((i, j))
        } else if tomatoBox[i][j] == 0 {
            // 덜익은 토마토 -1 로 표시
            distance[i][j] = -1
        }
    }
}

var idx = 0
let dx = [1, -1, 0, 0]
let dy = [0, 0, 1, -1]

while idx < queue.count {

    let (currentX, currentY) = queue[idx]
    idx += 1

    for i in 0...3 {
        let newX = currentX + dx[i]
        let newY = currentY + dy[i]

        if newX < 0 || newX >= N || newY < 0 || newY >= M { continue }
        if distance[newX][newY] >= 0 { continue }

        queue.append((newX, newY))
        distance[newX][newY] = distance[currentX][currentY] + 1
    }
}

var time = 0
for i in 0..<N {
    for j in 0..<M {
        if distance[i][j] == -1 {
            print(-1)
            exit(0)
        }
        time = max(time, distance[i][j])
    }
}
print(time)
