//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/02/27.
//  LeetCode > 6 > Zigzag Conversion

import Foundation
class Solution {
    func convert(_ s: String, _ numRows: Int) -> String {
        var answer: String = ""
        
        var stringArray: [[String.Element]] = Array(repeating: [], count: min(s.count,numRows))
        let originalStringArray = Array(s)
        if numRows == 1 { return s }

        var row = 0
        var isAscending = false

        for element in originalStringArray {

            stringArray[row].append(element)
            if (row == 0 || row == numRows - 1) { isAscending.toggle() }
            row += isAscending ? 1 : -1

        }
        
        for i in 0..<stringArray.count {
            answer += stringArray[i].map { String($0) }.joined()
        }

        return answer
    }
}

//let a = Solution()
//
//print(a.convert("PAYPALISHIRING", 4))
