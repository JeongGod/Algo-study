//
//  File.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/03/25.
//  Programmers > 월간 코드 챌린지 시즌1 > 쿼드압축 후 개수 세기

import Foundation

func solution(_ arr: [[Int]]) -> [Int] {

    let length: Int = arr.count

    var numberOfZero = 0
    var numberOfOne = 0

    func quad(_ arr: [[Int]], _ x: Int, _ y: Int, _ length: Int) {

        let start = arr[x][y]
        var isDuplicate = false

        for i in (x..<x + length) {
            if isDuplicate { break }
            for j in (y..<y + length) {
                if arr[i][j] != start {
                    quad(arr, x, y, length / 2)
                    quad(arr, x, y + length / 2, length / 2)
                    quad(arr, x + length / 2, y, length / 2)
                    quad(arr, x + length / 2, y + length / 2, length / 2)
                    isDuplicate = true
                    break
                }
            }
        }

        if !isDuplicate {
            if arr[x][y] == 0 {
                numberOfZero += 1
            } else {
                numberOfOne += 1
            }
        }
    }
    
    quad(arr, 0, 0, length)

    return [numberOfZero, numberOfOne]
}


