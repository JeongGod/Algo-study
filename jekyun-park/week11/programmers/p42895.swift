//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/03/09.
//  Programmers > 동적 계획법(Dynamic Programming) > N으로 표현

import Foundation

func solution(_ N: Int, _ number: Int) -> Int {

    if N == number { return 1 }

    var answer: Int = -1

    func dfs(_ count: Int, _ current: Int) {
        
        if count > 8 { return }
        
        if current == number {
            if count < answer || answer == -1 {
                answer = count
            }
            return
        }

        var newN = 0

        for i in 0..<8 {
            
            if answer != -1 && answer < count + 1 + i {
                break
            }
            
            newN = newN * 10 + N
            
            dfs(count + 1 + i, current + newN)
            dfs(count + 1 + i, current - newN)
            dfs(count + 1 + i, current * newN)
            dfs(count + 1 + i, current / newN)
        }
    }

    dfs(0, 0)

    return answer
}



