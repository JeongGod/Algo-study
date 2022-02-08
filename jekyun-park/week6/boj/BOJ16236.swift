//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/02/07.
//  BOJ 16236 아기상어


import Foundation

func bfs(_ row: Int, _ column: Int, _ size: Int) -> (Int, Int, Int) {
    var visited: [[Bool]] = Array(repeating: Array(repeating: false, count: N), count: N)
    var distanceToNearestFish = Int(1e9)

    var queue: [(Int, Int, Int)] = []
    var fishes: [(Int, Int, Int)] = []

    visited[row][column] = true
    queue.append((row, column, 0))

    var idx = 0

    while idx < queue.count {

        let (r, c, dist) = queue[idx]
        idx += 1

        for i in 0..<4 {
            let newRow = r + dx[i]
            let newColumn = c + dy[i]

            if newRow < 0 || newRow >= N || newColumn < 0 || newColumn >= N || space[newRow][newColumn] > size { continue }

            if !visited[newRow][newColumn] {
                visited[newRow][newColumn] = true

                // 물고기가 상어보다 작은크기이고, 가장 가까운 물고기와의 거리보다 작다면
                if (0 < space[newRow][newColumn]) && (space[newRow][newColumn] < size) && (dist + 1 <= distanceToNearestFish) {
                    distanceToNearestFish = dist + 1
                    fishes.append((newRow, newColumn, distanceToNearestFish))
                } else {
                    queue.append((newRow, newColumn, dist + 1))
                }
            }
        }
    }

    if !fishes.isEmpty {
        fishes.sort(by: {
            if $0.2 == $1.2 {
                if $0.0 == $1.0 {
                    return $0.1 < $1.1
                } else {
                    return $0.0 < $1.0
                }
            } else {
                return $0.2 < $1.2
            }
        })
        return fishes[0]
    } else {
        return (0, 0, 0)
    }
}

let N = Int(readLine()!)!
var space: [[Int]] = []
for _ in 0..<N { space.append(readLine()!.split(separator: " ").map { Int($0)! }) }
var shark: (row: Int, column: Int, size: Int) = (0, 0, 2)
let dx = [-1, 1, 0, 0]
let dy = [0, 0, -1, 1]

for i in 0..<N {
    for j in 0..<N {
        if space[i][j] == 9 {
            shark.row = i
            shark.column = j
        }
    }
}


var time = 0
var ateCount = 0
//print("yaho")

while true {

    let (row, column, distance) = bfs(shark.row, shark.column, shark.size)

    if (row, column, distance) == (0, 0, 0) { print(time);break }
    time += distance
    ateCount += 1

    space[row][column] = 9
    space[shark.row][shark.column] = 0
    shark.row = row
    shark.column = column


    if ateCount == shark.size {
        shark.size += 1
        ateCount = 0
    }

}
