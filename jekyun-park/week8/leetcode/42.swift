//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/02/20.
// LeetCode > 42 > Trapping Rain Water 

import Foundation

class Solution {
    func trap(_ height: [Int]) -> Int {

        var left = 0
        var right = height.count - 1
        var answer: Int = 0
        var leftMax = 0, rightMax = 0

        while left < right {
            if height[left] < height[right] {
                if height[left] >= leftMax {
                    leftMax = height[left]
                } else {
                    answer += leftMax - height[left]
                }
                left += 1
            } else {
                if height[right] >= rightMax {
                    rightMax = height[right]
                } else {
                    answer += rightMax-height[right]
                }
                right -= 1
            }
        }
        return answer
    }
}

// let a = Solution()

// print(a.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
