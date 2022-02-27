//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/02/27.
//  LeetCode > 48 > Rotate Image
    
import Foundation

class Solution {
    func rotate(_ matrix: inout [[Int]]) {
        var newMatrix: [[Int]] = []
        
        for i in 0..<matrix.count {
            var line: [Int] = []
            for j in (0..<matrix.count).reversed() {
                line.append(matrix[j][i])
            }
            newMatrix.append(line)
        }
        matrix = newMatrix
    }
}

//let a = Solution()
//
//var map = [[1,2,3],[4,5,6],[7,8,9]]
//print(a.rotate(&map))
