//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/05/22.
//  LeetCode > 56. Merge Intervals

import Foundation

class Solution {
    func merge(_ intervals: [[Int]]) -> [[Int]] {
        if intervals.count < 1 { return intervals }
        let intervals = intervals.sorted { $0[0] < $1[0] }
        var answer: [[Int]] = [intervals[0]]

        for i in 1..<intervals.count {

            let interval = intervals[i]
            let lastIndex = answer.count - 1

            if overlap(answer[lastIndex], interval) {
                answer[lastIndex] = [min(answer[lastIndex][0], interval[0]),max(answer[lastIndex][1], interval[1])]
            } else {
                answer.append(interval)
            }
        }

        return answer
    }

    func overlap(_ a: [Int], _ b: [Int]) -> Bool {
        return !(b[0] > a[1])
    }

}

//let a = Solution()
//print(a.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
