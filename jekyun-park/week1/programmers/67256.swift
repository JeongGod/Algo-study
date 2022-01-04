//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/01/01.
// 2020 카카오 인턴십 : 키패드 누르기 

import Foundation

func isLeft(_ number:Int) -> Bool {
    return (number == 1 || number == 4 || number == 7)
}

func isRight(_ number:Int) -> Bool {
    return (number == 3 || number == 6 || number == 9)
}


func solution(_ numbers:[Int], _ hand:String) -> String {
    var answer : String = ""
    
    // 10 -> * , 11 -> # 이라고 가정
    
    let keyPad = [(3,1),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(3,0),(3,2)] // 0,1,2,...,*,#
    var currentLeftThumb = (3,0)
    var currentRightThumb = (3,2)
    
    
    for number in numbers {
        
        let coord = keyPad[number]
        
        if isLeft(number) {
            answer += "L"
            currentLeftThumb = keyPad[number]
        } else if isRight(number) {
            answer += "R"
            currentRightThumb = keyPad[number]
        } else {
            let distanceWithLeftThumb = abs(coord.0-currentLeftThumb.0) + abs(coord.1-currentLeftThumb.1)
            let distanceWithRightThumb = abs(coord.0-currentRightThumb.0) + abs(coord.1-currentRightThumb.1)
            if distanceWithLeftThumb > distanceWithRightThumb {
                answer += "R"
                currentRightThumb = keyPad[number]
            } else if distanceWithLeftThumb < distanceWithRightThumb {
                answer += "L"
                currentLeftThumb = keyPad[number]
            } else {
                if hand == "left" {
                    answer += "L"
                    currentLeftThumb = keyPad[number]
                } else {
                    answer += "R"
                    currentRightThumb = keyPad[number]
                }
            }
            
        }
    }
    
    return answer
}

/* 1,4,7 -> 왼손엄지
   3,6,9 -> 오른엄지
   2,5,8,0 -> 두 엄지중 현재 키패드의 위치에서 가까운 엄지 사용 -> 거리가 같을시 오른손잡이는 오른손엄지, 왼손잡이는 왼손엄지
 
 numbers -> 번호를 누를 순서 배열
 hand -> "left" or "right"
 
 */

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
