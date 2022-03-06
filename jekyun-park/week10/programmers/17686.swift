//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/03/05.
//  2018 KAKAO BLIND RECRUITMENT > 파일명 정렬

import Foundation

func solution(_ files: [String]) -> [String] {

    let newFiles = files.map { file -> (String, [String]) in
        var head: [Character] = [], number: [Character] = []

        for character in file {
            let char = Character(extendedGraphemeClusterLiteral: character)

            if head.isEmpty {
                head.append(char)
            } else {
                if !char.isNumber, number.isEmpty {
                    head.append(char)
                } else if char.isNumber, !head.isEmpty {
                    number.append(char)
                } else if !char.isNumber, !head.isEmpty, !number.isEmpty {
                    break
                }
            }
        }
        return (file, [head.map{ String($0) }.joined(), number.map { String($0) }.joined()])
    }

    let sortedNewFiles = newFiles.sorted { (a, b) -> Bool in
        let lhs = a.1
        let rhs = b.1
        
        for (leftString,rightString) in zip(lhs, rhs) {
            if leftString.lowercased() != rightString.lowercased() {
                guard let fi = Int(leftString) else {
                    return leftString.lowercased() < rightString.lowercased()
                }
                if fi != Int(rightString)! {
                    return fi < Int(rightString)!
                }
            }
        }
        return false
    }.map { $0.0 }
    
    return sortedNewFiles
}

//print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
////출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
//print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
////출력: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
