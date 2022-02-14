//
//  main2.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/02/10.
//

import Foundation

func solution(_ n: Int, _ t: Int, _ m: Int, _ timetable: [String]) -> String {

    let crews = timetable.map { stringToMinute($0) }.sorted()
    let numberOfCrews = crews.count
    var answer: Int = 0
    let shuttles: [Int] = {
        var shuttles: [Int] = []
        let startTime = 9 * 60

        for i in 0..<n {
            shuttles.append(startTime + t * i)
        }

        return shuttles
    }()

    var crewIndex = 0

    for shuttle in shuttles {
        var count: Int = 0

        while (count < m) && crewIndex < numberOfCrews && crews[crewIndex] <= shuttle {
            count += 1
            crewIndex += 1
        }

        answer = count < m ? shuttle : crews[crewIndex - 1] - 1

        if crewIndex > numberOfCrews { break }

    }

    let hour: String = String(format: "%02d", answer / 60)
    let minute: String = String(format: "%02d", answer % 60)


    return "\(hour):\(minute)"
}

func stringToMinute(_ str: String) -> Int {

    let strArr = Array(str)
    let hour: Int = Int(String(strArr[...1]))!
    let minute: Int = Int(String(strArr[3...]))!

    return hour * 60 + minute
}

//print(solution(2, 10, 1, ["11:12"]))
