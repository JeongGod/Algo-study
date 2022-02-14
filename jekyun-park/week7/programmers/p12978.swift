//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/02/10.
//

import Foundation

func solution(_ N: Int, _ road: [[Int]], _ k: Int) -> Int {
    var town: [[Int]] = Array(repeating: Array(repeating: 0, count: N + 1), count: N + 1)

    for array in road {
        if town[array[0]][array[1]] != 0 {
            town[array[0]][array[1]] = max(town[array[0]][array[1]], array[2])
        } else {
            town[array[0]][array[1]] = array[2]
        }
    }
    
    var queue: [Int] = [1]
    var distances = [Int](repeating: Int.max, count: N + 1)
    distances[1] = 0

    while !queue.isEmpty {

        let first = queue.removeFirst()

        let filtered = road.filter { $0[0] == first || $0[1] == first }

        for road in filtered {

            let connectedTown = road[0] == first ? road[1] : road[0]

            if distances[first] == Int.max { continue }

            if distances[first] + road[2] < distances[connectedTown] {
                distances[connectedTown] = distances[first] + road[2]
                queue.append(connectedTown)
            }
        }
    }
    
    return distances.filter { $0 <= k }.count
}

print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))
