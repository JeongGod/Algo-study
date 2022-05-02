//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/04/29.
//  Programmers > 위클리 챌린지 > 모음사전

import Foundation

func solution(_ word:String) -> Int {
    
    var answer = 0
    let dictionary: [String:Int] = ["A":0,"E":1,"I":2,"O":3,"U":4]
    let countArray = [781,156,31,6,1]
    
    answer = word.enumerated().map { countArray[$0.offset] * dictionary[String($0.element)]! }.reduce(word.count) { $0 + $1 }
    
    /*
     index 0 1 2 3 4
     
     A
     AA
     AAA
     AAAA
     AAAAA
     AAAAE
     AAAAI
     AAAAO
     AAAAU
     AAAE
     AAAEA
     AAAEE
     AAAEI
     AAAEO
     AAAEU
     AAAI
     
     */
    
    return answer
}
