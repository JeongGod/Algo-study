//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/02/15.
// LeetCode > 44 > Wildcard Matching

import Foundation

class Solution {
    func isMatch(_ s: String, _ p: String) -> Bool {
        var sPointer = 0
        var pPointer = 0
        var match = 0
        var star = -1

        while sPointer < s.count {
            if pPointer < p.count && (s[s.index(s.startIndex, offsetBy: sPointer)] == p[p.index(p.startIndex, offsetBy: pPointer)] || p[p.index(p.startIndex, offsetBy: pPointer)] == "?") {
                sPointer += 1
                pPointer += 1
            } else if pPointer < p.count && p[p.index(p.startIndex, offsetBy: pPointer)] == "*" {
                star = pPointer
                match = sPointer
                pPointer += 1
            } else if star != -1 {
                pPointer = star + 1
                match += 1
                sPointer = match
            } else {
                return false
            }
        }

        while pPointer < p.count && p[p.index(p.startIndex, offsetBy: pPointer)] == "*" {
            pPointer += 1
        }

        return pPointer == p.count
    }
    func isMatchFailed(_ s: String, _ p: String) -> Bool {

        var pattern: String = ""

        for char in p {
            if char == "?" {
                pattern.append(".")
            } else if char == "*" {
                pattern.append(".*")
            } else {
                pattern.append(char)
            }
        }

        let pred = NSPredicate(format: "SELF MATCHES %@", pattern)

        return pred.evaluate(with: s)
    }
}

//let a = Solution()
//print(a.isMatch("aa", "a"))
//print(a.isMatch("aa", "*"))
//print(a.isMatch("cb", "?a"))
