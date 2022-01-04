//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/01/04.
//

import Foundation

func solution(_ k:Int, _ dungeons:[[Int]]) -> [Int] {
    
    // k = 피로도
    // 최소 피로도, 소모 피로도 dungeons[0][0], dungeons[0][1]
    
    dungeons.indices
    var answers : [Int] = []
    let numOfdungeons = dungeons.count
    
    let candidates = findAllCase(numOfdungeons)
    
    for candidate in candidates { // candidate = 던전 도는 순서가 담긴 배열
        var tiredPoint = k // 현재 피로도
        var passedDungeons = 0
        for num in candidate { // num = 던전 번호
            if tiredPoint < dungeons[num][0] { // 현재 피로도가 던전의 최소 피로도보다 작다면
                break
            } else { // 현재 피로도가 던전의 최소 피로도보다 크거나 같다면
                tiredPoint -= dungeons[num][1]
                passedDungeons += 1
            }
        }
        answers.append(passedDungeons)
    }
    print(answers.max()!)
    return answers
}

func findAllCase(_ n:Int) -> [[Int]] {
    
    var result : [[Int]] = []
    var visited : [Bool] = Array(repeating: false, count: n)
    
    func permute(_ arr:[Int]) {
        if arr.count == n {
            result.append(arr)
           return
        }
        for i in 0..<n {
            if visited[i] {
                continue
            } else {
                visited[i] = true
                permute(arr+[Array(0..<n)[i]])
                visited[i] = false
            }
        }
    }
    permute([])
    return result
}

print(solution(80, [[80,20],[50,40],[30,10]]))
