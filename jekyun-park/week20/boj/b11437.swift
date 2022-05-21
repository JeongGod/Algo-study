//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/05/20.
//  BOJ > 11437 > LCA(Lowest Common Ancestor)

import Foundation


let N = Int(readLine()!)!
var tree = Array(repeating: [Int](), count: N + 1)
var parent = Array(repeating: 0, count: N + 1)
var depth = Array(repeating: 0, count: N + 1)
var visited = Array(repeating: false, count: N + 1)

for _ in 0..<N - 1 {
    let uv = readLine()!.split(separator: " ").map { Int($0)! }
    let u = uv.first!, v = uv.last!
    tree[u].append(v)
    tree[v].append(u)
}

func dfs(_ n: Int, _ d: Int) {
    visited[n] = true
    depth[n] = d

    for node in tree[n] {
        if visited[node] {
            continue
        }
        parent[node] = n
        dfs(node, d + 1)
    }
}

func lca(_ a: inout Int, _ b: inout Int) -> Int {

    while depth[a] != depth[b] {
        if depth[a] > depth[b] {
            a = parent[a]
        } else {
            b = parent[b]
        }
    }

    while a != b {
        a = parent[a]
        b = parent[b]
    }

    return a
}

dfs(1, 0)

let M = Int(readLine()!)!
for _ in 0..<M {
    let uv = readLine()!.split(separator: " ").map { Int($0)! }
    var u = uv.first!, v = uv.last!
    print(lca(&u, &v))
}
