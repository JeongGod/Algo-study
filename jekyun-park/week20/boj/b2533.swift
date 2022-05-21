//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/05/20.
//  BOJ > 2533 > 사회망 서비스

import Foundation

let N = Int(readLine()!)!

var tree = Array(repeating: [Int](), count: N + 1)

for _ in 0..<N - 1 {
    let uv = readLine()!.split(separator: " ").map { Int($0)! }
    let u = uv.first!, v = uv.last!
    tree[u].append(v)
    tree[v].append(u)
}

var dp = Array(repeating: [0, 0], count: N + 1)
var visited = Array(repeating: false, count: N + 1)

func dfs(_ n:Int) {
    visited[n] = true
    dp[n][0] = 1
    for i in tree[n] {
        if !visited[i] {
            dfs(i)
            dp[n][0] += min(dp[i][0], dp[i][1])
            dp[n][1] += dp[i][0]
        }
    }
}

dfs(1)
print(min(dp[1][0], dp[1][1]))
