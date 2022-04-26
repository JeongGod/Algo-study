//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/04/21.
//  BOJ > 18500 > 미네랄2

/*
 왼쪽 오른쪽 왼쪽 오른쪽 번갈아가면서 막대를 던진다.
 막대를 던지고나면 막대가 날아가다가 미네랄이 있다면 미네랄이 파괴되고 막대는 이동을 멈춘다.
 미네랄이 파괴되고나서 클러스터가 분리될 수도 있기 때문에 확인해본다.
 클러스터가 떠있다면 중력이 작용하여 아래로 떨어지게 된다.
 */

import Foundation

let RC = readLine()!.split(separator: " ").map { Int($0)! }
let R = RC[0]; let C = RC[1]
var map: [[String]] = []

for _ in 0..<R {
    map.append(readLine()!.map { String($0) })
}

var N = Int(readLine()!)!
var heights = readLine()!.split(separator: " ").map { Int($0)! }
var queue: [(Int, Int)] = []
var direction = 1

let dx = [1, -1, 0, 0]
let dy = [0, 0, 1, -1]

func throwStick(_ x: Int, _ direction: Int) {
    let x = R - x
    var y = 0
    if direction == 1 {
        for i in 0..<C {
            if map[x][i] == "x" {
                map[x][i] = "."
                y = i
                break
            }
        }
    } else {
        for i in stride(from: C - 1, to: -1, by: -1) {
            if map[x][i] == "x" {
                map[x][i] = "."
                y = i
                break
            }
        }
    }

    for i in 0..<4 {
        let nx = x + dx[i]
        let ny = y + dy[i]

        if (0 <= nx && nx < R) && (0 <= ny && ny < C) {
            if map[nx][ny] == "x" {
                queue.append((nx, ny))
            }
        }
    }
}

func bfs(_ x: Int, _ y: Int) {
    var bfsQueue: [(Int, Int)] = []
    var visited = Array(repeating: Array(repeating: 0, count: C), count: R)
    var candidates: [(Int, Int)] = []
    bfsQueue.append((x, y))

    while !bfsQueue.isEmpty {
        let (x, y) = bfsQueue.removeFirst()

        if x == R - 1 {
            return
        }

        // 아래칸이 빈칸이라면
        if map[x + 1][y] == "." {
            candidates.append((x, y))
        }
        // 4방향 순회
        for i in 0..<4 {
            let nx = x + dx[i]
            let ny = y + dy[i]
            // 순회할 칸이 범위안에 들어오고, 방문하지 않은 미네랄이면 큐에 삽입
            if (0 <= nx && nx < R) && (0 <= ny && ny < C) {
                if map[nx][ny] == "x" && (visited[nx][ny] == 0) {
                    visited[nx][ny] = 1
                    bfsQueue.append((nx, ny))
                }
            }
        }
    }

    gravity(visited, candidates)
}

func gravity(_ visited: [[Int]], _ candidates: [(Int, Int)]) {

    var k = 1 ; var flag = 0

    while true {
        for (i, j) in candidates {
            if i + k == R - 1 {
                flag = 1
                break
            }

            if map[i + k + 1][j] == "x" && (visited[i + k + 1][j] == 0) {
                flag = 1
                break
            }
        }
        if (flag != 0) { break }
        k += 1
    }

    for i in stride(from: R - 2, to: -1, by: -1) {
        for j in 0..<C {
            if map[i][j] == "x" && (visited[i][j] == 1){
                map[i][j] = "."
                map[i + k][j] = "x"
            }
        }
    }
}

while N > 0 {
    let index = heights.removeFirst()
    throwStick(index, direction)

    while !queue.isEmpty {
        let (x, y) = queue.removeFirst()
        bfs(x, y)
    }

    direction *= -1
    N -= 1
}

for i in 0..<R {
    for j in 0..<C {
        print(map[i][j], terminator: "")
    }
    print()
}
