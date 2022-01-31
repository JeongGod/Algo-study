//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/01/28.
//

import Foundation

func solution(_ fees: [Int], _ records: [String]) -> [Int] {

    var timeRecord: [String: [[String]]] = [:]
    var feeDictionary: [String:Int] = [:]


    for record in records {
        let log = record.split(separator: " ")
        let time = String(log[0])
        let car = String(log[1])
//        let inOut = log[2]

        if timeRecord[car] == nil {
            timeRecord[car] = []
            timeRecord[car]?.append([time])
        } else {
            if timeRecord[car]![timeRecord[car]!.count - 1].count == 2 {
                timeRecord[car]!.append([time])
            } else {
                timeRecord[car]![timeRecord[car]!.count - 1].append(time)
            }
        }
    }

    for log in timeRecord {
        if log.value.last!.count % 2 != 0 {
            timeRecord[log.key]![timeRecord[log.key]!.count - 1].append("23:59")
        }
    }
    
    
    
    for car in timeRecord {
        var sum = 0
        timeRecord[car.key]!.forEach {
            sum += calculateTime($0[0],$0[1])
        }
        feeDictionary[car.key] = calculateFee(sum, fees)
    }

    var answer:[Int] = []
    feeDictionary.sorted(by: <).forEach { answer.append($0.value) }

    return answer
}




func calculateFee(_ parkTime: Int, _ fees: [Int]) -> Int {
    
    let standardTime = fees[0]
    let standardFee = fees[1]
    let unitTime = fees[2]
    let unitFee = fees[3]
    if parkTime <= standardTime { return standardFee }
    let totalFee = standardFee + Int(ceil(Double(parkTime - standardTime) / Double(unitTime))) * unitFee

    return totalFee
}

func calculateTime(_ x: String, _ y: String) -> Int {

    let xHourToMinute: Int = Int(x[x.startIndex...x.index(x.startIndex, offsetBy: 1)])! * 60
    let xMinute: Int = Int(x[x.index(x.startIndex, offsetBy: 3)...x.index(x.startIndex, offsetBy: 4)])!
    let yHourToMinute: Int = Int(y[y.startIndex...y.index(y.startIndex, offsetBy: 1)])! * 60
    let yMinute: Int = Int(y[y.index(y.startIndex, offsetBy: 3)...y.index(y.startIndex, offsetBy: 4)])!

    return (yHourToMinute + yMinute) - (xHourToMinute + xMinute)
}

//print(calculateTime("18:59", "23:59"))

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

//print(solution([120, 0, 60, 591], ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
