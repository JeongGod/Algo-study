//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/02/08.
//

import Foundation

func solution(_ s:String) -> Int{
    
    var stack = [String.Element]()
    
    for i in s {
        if stack.count > 0, stack.last == i {
            stack.popLast()
        } else {
            stack.append(i)
        }
    }
    return stack.isEmpty ? 1 : 0
}

print(solution("baabaa"))
print(solution("cdcd"))
