//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/04/22.
//

import Foundation

let commands = readLine()!.split(separator: " ").map { Int($0)! }
let costs: [Int: [(destination: Int, cost: Int)]] = [0: [(1, 2), (2, 2), (3, 2), (4, 2)], 1: [(1, 1), (2, 3), (3, 4), (4, 3)], 2: [(1, 3), (2, 1), (3, 3), (4, 4)], 3: [(1, 4), (2, 3), (3, 1), (4, 3)], 4: [(1, 3), (2, 4), (3, 3), (4, 1)]]
var dp = Array(repeating: Array(repeating: Array(repeating: -1, count: 5), count: 5), count: 100000)

func solve(_ n: Int, _ L: Int, _ R: Int) -> Int {

    if n >= commands.count - 1 { return 0 }

    if dp[n][L][R] != -1 {
        return dp[n][L][R]
    }

    dp[n][L][R] = min(solve(n + 1, commands[n], R) + costs[L]![commands[n] - 1].cost, solve(n + 1, L, commands[n]) + costs[R]![commands[n] - 1].cost)
    return dp[n][L][R]
}

print(solve(0, 0, 0))
