//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/03/06.
// BOJ > 15685 > 드래곤 커브

import Foundation

let n = Int(readLine()!)!
var dragonCurves: [[Int]] = []
var map = Array(repeating: Array(repeating: false, count: 101), count: 101)
let dx = [0, -1, 0, 1]
let dy = [1, 0, -1, 0]
var stack: [Int] = []
var endPoint: (x: Int, y: Int) = (0, 0)
var answer = 0

for _ in 0..<n {
    let dragonCurveInfo = readLine()!.split(separator:" ").map { Int($0)! }
    dragonCurves.append(dragonCurveInfo)
}

func makeDragonCurveGenerations() {
    let size = stack.count

    for i in stride(from: size-1, to: -1, by: -1) {
        let dir = (stack[i] + 1) % 4

        endPoint.x = endPoint.x + dx[dir]
        endPoint.y = endPoint.y + dy[dir]

        map[endPoint.x][endPoint.y] = true

        stack.append(dir)
    }

}
// x,y,d,g
// 0: x좌표가 증가하는 방향 (→)
// 1: y좌표가 감소하는 방향 (↑)
// 2: x좌표가 감소하는 방향 (←)
// 3: y좌표가 증가하는 방향 (↓)

for dragonCurve in dragonCurves {

    stack.removeAll()

    let x = dragonCurve[1]
    let y = dragonCurve[0]
    let d = dragonCurve[2]
    let g = dragonCurve[3]

    endPoint.x = x
    endPoint.y = y

    map[endPoint.x][endPoint.y] = true

    endPoint.x = x + dx[d]
    endPoint.y = y + dy[d]

    map[endPoint.x][endPoint.y] = true

    stack.append(d)

    for _ in 0..<g {
        makeDragonCurveGenerations()
    }
}

for i in 0..<101 {
    for j in 0..<101 {
        if map[i][j] && map[i + 1][j] && map[i][j + 1] && map[i + 1][j + 1] {
            answer += 1
        }
    }
}

print(answer)





