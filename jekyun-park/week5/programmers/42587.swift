//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/01/26.
// Programmers > 스택/큐 > 프린터

import Foundation

func solution(_ priorities: [Int], _ location: Int) -> Int {

    // key : 문서 index , value : 우선순위
    var dictionary: [Int: Int] = [:]

    for i in 0..<priorities.count {
        dictionary[i] = priorities[i]
    }

    var stack = Array(dictionary)
    var printed: [(key:Int,value:Int)] = []
    stack.sort(by: <)
    
    while !stack.isEmpty {
        let (index,priority) = stack.removeFirst()
        
        if stack.contains(where: { $0.value > priority }) == true {
            stack.append((key:index,value:priority))
        } else {
            printed.append((key:index,value:priority))
        }
    }
    return printed.firstIndex { $0.key == location }! + 1
}

print(solution([2, 1, 3, 2], 2)) // 1
print(solution([1, 1, 9, 1, 1, 1], 0)) // 5
