//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/01/10.
//

import Foundation

import Foundation

func solution(_ operations:[String]) -> [Int] {
    
    var maxQueue:[Int] = []
    var minQueue:[Int] = []
    
    var queue:[Int] = []
    
    for operation in operations {
        if operation[operation.startIndex] == "I" {
            let split = operation.components(separatedBy: " ")
            queue.append(Int(split[1])!)
            
            
        } else if operation == "D 1" { // 최대값 삭제
            if queue.isEmpty { continue }
            
            queue.sort(by: <)
            queue.removeLast()
            
            
        } else if operation == "D -1" { // 최솟값 삭제
            if queue.isEmpty { continue }
            
            queue.sort(by: <)
            queue.removeFirst()
        }
    }
    
    
    if queue.isEmpty { return [0,0] } else { return [queue.max()!,queue.min()!]}
}



print(solution(["I 16","D 1"])) // [0,0]
print(solution(["I 7","I 5","I -5","D -1"])) // [7,5]

