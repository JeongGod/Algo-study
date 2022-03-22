//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/03/22.
//  Programmers > 월간 코드 챌린지 시즌3 > n^2 배열 자르기 (87390)

import Foundation

//func solution(_ n:Int, _ left:Int64, _ right:Int64) -> [Int] {
//
//    var array: [[Int]] = Array(repeating:[],count:n)
//
//    for i in array.indices {
//        array[i].append(contentsOf: (i+1)...n)
//
//        let newArray = Array(repeating: i+1, count: i)
//        array[i] = newArray + array[i]
//    }
//
//    let answer = array.flatMap { $0 }
//
//    let leftIndex = answer.index(answer.startIndex, offsetBy: Int(left))
//    let rightIndex = answer.index(answer.startIndex, offsetBy: Int(right))
//
//    return Array(answer[leftIndex...rightIndex])
//}

// -> 전체 배열 구하기 : 시간초과

func solution(_ n: Int, _ left: Int64, _ right: Int64) -> [Int] {

    let left = Int(left)
    let right = Int(right)

    let size = right - left + 1

    let leftGroupNumber = left / n
    let leftIndexNumber = left % n

    let rightGroupNumber = right / n
//    let rightIndexNumber = right % n

    var answer: [Int] = []

    for i in (leftGroupNumber)...(rightGroupNumber) {

        let array = Array(repeating: i + 1, count: i) + Array((i + 1)...n)
        answer.append(contentsOf: array)

    }

    return Array(answer[leftIndexNumber..<leftIndexNumber+size])
}


//print(solution(3, 2, 5))
//print(solution(4, 7, 14))
