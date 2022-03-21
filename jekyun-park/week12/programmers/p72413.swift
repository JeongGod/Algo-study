//
//  main.swift
//  AlgorithmStudy
//
//  Created by 박제균 on 2021/09/09.
//

import Foundation

func solution(_ n: Int, _ s: Int, _ a: Int, _ b: Int, _ fares: [[Int]]) -> Int {

    let maxValue: Int = 20000000

    var arr = Array(repeating: Array(repeating: maxValue, count: n), count: n)

    for fare in fares {
        let startNode = fare[0] - 1
        let destinationNode = fare[1] - 1
        let cost = fare[2]

        arr[startNode][destinationNode] = cost
        arr[destinationNode][startNode] = cost
    }


    for i in 0..<n {
        for j in 0..<n {
            if arr[j][i] == maxValue || i == j {
                continue
            }
            for k in 0..<n {
                if j == k {
                    continue
                }
                arr[j][k] = min(arr[j][i] + arr[i][k], arr[j][k])
            }
        }
    }

    var minFare = arr[s - 1][a - 1] + arr[s - 1][b - 1]

    for i in 0..<n {
        let start = arr[s - 1][i]
        let a = a - 1 == i ? 0 : arr[i][a - 1]
        let b = b - 1 == i ? 0 : arr[i][b - 1]
        minFare = min(minFare, start + a + b)
    }

    return minFare
}

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))


