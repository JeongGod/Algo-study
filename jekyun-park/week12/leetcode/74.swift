//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/03/15.
//  LeetCode > 74. Search a 2D Matrix

import Foundation

class Solution {
    func searchMatrix(_ matrix: [[Int]], _ target: Int) -> Bool {

        let n = matrix.count
        
        if n == 0 { return false }

        for index in 0..<n {
            if matrix[index][0] > target {
                if index == 0 {
                    return false
                }
                return binarySearch(matrix[index - 1], target, 0, matrix[index-1].count)
            }
            if index == n - 1 {
                return binarySearch(matrix[index], target, 0, matrix[index].count)
            }
        }
        return false
    }

    func binarySearch(_ arr: [Int], _ target: Int, _ start: Int, _ end: Int) -> Bool {

        if start >= end {
            return false
        }

        let mid = (start + end) / 2

        if arr[mid] == target {
            return true
        } else if arr[mid] < target {
            return binarySearch(arr, target, mid + 1, end)
        } else {
            return binarySearch(arr, target, start, mid)
        }
    }

}

