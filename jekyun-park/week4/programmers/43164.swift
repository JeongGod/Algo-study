//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/01/20.
//

import Foundation

func solution(_ tickets: [[String]]) -> [String] {

    var visited = Array(repeating: false, count: tickets.count)
    let tickets = tickets.sorted { $0[1] < $1[1] }
    var path: [String] = []

    func dfs(_ city: String) {
        if path.count == tickets.count {
            path.append(city)
            return
        }

        for i in 0..<tickets.count {
            let start = tickets[i][0]
            let end = tickets[i][1]

            if city == start, visited[i] == false {
                visited[i] = true
                path.append(start)
                dfs(end)

                if path.count == tickets.count + 1 {
                    return
                }

                // 해당 도시에 갈 수 없으면 취소함
                path.removeLast()
                visited[i] = false
            }
        }
    }
    dfs("ICN")
    return path
}

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
