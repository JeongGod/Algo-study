//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/05/16.
//

import Foundation

let N = Int(readLine()!)!
var villages: [[Int]] = []
var people = 0

for _ in 0..<N {
    let village = readLine()!.split(separator: " ").map { Int($0)! }
    villages.append(village)
    people += village[1]
}
villages.sort { $0[0] > $1[1] }
var count = 0
var answer = 0

let mid = people % 2 == 0 ? people/2 : people/2+1

for i in 0..<N {
    count += villages[i][1]
    if count >= mid {
        answer = villages[i][0]
        break
    }
}

print(answer)
