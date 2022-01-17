//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/01/16.
//

import Foundation

func solution(_ s:String) -> Int {
    
    var answer: Int = 0
    let stringToRotate = s
    
    for x in 0..<s.count {
        
        if isCorrectParentheses((rotatedString(stringToRotate, x))) {
            answer += 1
        }
        
    }
    
    return answer
}


func isCorrectParentheses(_ str:String) -> Bool {
    
    var stack: [String.Element] = []
    var parantheses = str
    
    
    while true {
        
        let char = parantheses.removeFirst()
        
        if char == "(" || char == "{" || char == "[" {
            stack.append(char)
        } else if char == "}" {
            if stack.last != "{" || stack.isEmpty {
                return false
            }
            stack.popLast()
        } else if char == ")" {
            if  stack.last != "(" || stack.isEmpty {
                return false
            }
            stack.popLast()
        } else if char == "]" {
            if stack.last != "[" || stack.isEmpty {
                return false
            }
            stack.popLast()
        }
        
        if parantheses.count == 0 { break }
    }
    
    if stack.isEmpty {
        return true
        
    } else {
        return false }
    
}
    
func rotatedString(_ str:String, _ x:Int) -> String {
    
    let leftSubString = str[str.index(str.startIndex, offsetBy: x)..<str.index(str.endIndex, offsetBy: 0)]
    let rightSubString = str[str.index(str.startIndex, offsetBy: 0)..<str.index(str.startIndex, offsetBy: x)]
    let returnString:String = String(leftSubString) + String(rightSubString)
    
    return returnString
}

    

//print(isCorrectParentheses((rotatedString("[](){}", 5))))
//print((rotatedString("}]()[{", 5)))
//print(solution("[](){}"))

