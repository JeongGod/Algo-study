//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/03/15.
// > LeetCode > 55. Jump Game

import Foundation

class Solution {
    func canJump(_ nums: [Int]) -> Bool {

        guard var maxJumpDistance = nums.first else {
            // 빈 배열
            return true
        }

        for (index, value) in nums.enumerated() {

            if index > maxJumpDistance {
                return false
            }
            maxJumpDistance = max(maxJumpDistance, index + value)
        }
        return true
    }
}
