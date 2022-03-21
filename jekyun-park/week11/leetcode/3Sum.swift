//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/03/11.
//  LeetCode > 15. 3Sum

import Foundation

class Solution {
    func threeSum(_ nums: [Int]) -> [[Int]] {

        let nums = nums.sorted()
        let length = nums.count
        var answer: [[Int]] = []
        var index = 0

        while index < length {

            var start = index + 1
            var end = length - 1

            while start < end {

                let sum = nums[index] + nums[start] + nums[end]

                if sum <= 0 {
                    if sum == 0 { answer.append([nums[index], nums[start], nums[end]]) }

                    start += 1

                    while start < end && nums[start - 1] == nums[start] {
                        start += 1
                    }

                } else {
                    end -= 1

                    while start < end && nums[end + 1] == nums[end] {
                        end -= 1
                    }

                }

            }

            index += 1

            while index < length && nums[index - 1] == nums[index] {
                index += 1
            }

        }

        return answer
    }
}

//let a = Solution()
//print(a.threeSum([-1, 0, 1, 2, -1, -4]))

