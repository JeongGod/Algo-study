//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/05/13.
//  BOJ > 1092 > 배

import Foundation

let N = Int(readLine()!)!
var cranes = readLine()!.split(separator: " ").map { Int($0)! }
let M = Int(readLine()!)!
var boxes = readLine()!.split(separator: " ").map { Int($0)! }
cranes.sort(by: >)
boxes.sort(by:>)
var answer = 0

if cranes.max()! < boxes.max()! {
    print(-1)
    exit(0)
} else {
    while true {
        if boxes.isEmpty {
            break
        }

        for i in 0..<cranes.count {
            for j in 0..<boxes.count {
                if cranes[i] >= boxes[j] {
                    boxes.remove(at: j)
                    break
                }
            }
        }
        
        answer += 1
    }
}

print(answer)


