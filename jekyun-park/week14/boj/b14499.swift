//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/04/03.
//  BOJ > 14499 > 주사위 굴리기

import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let mapSize = (N: input[1], M: input[0])
var position = (x: input[2], y: input[3])
var map: [[Int]] = []
for _ in 0..<mapSize.M {
    map.append(readLine()!.split(separator: " ").map { Int($0)! })
}

let operations = readLine()!.split(separator: " ").map { Int($0)! }

let dice = Dice()

for op in operations {

    switch op {

    case 1:
        if position.y + 1 < mapSize.N {
            map[position.x][position.y + 1] = dice.move(op, map[position.x][position.y + 1])
            position.y += 1
        }
    case 2:
        if position.y - 1 >= 0 {
            map[position.x][position.y - 1] = dice.move(op, map[position.x][position.y - 1])
            position.y -= 1
        }
    case 3:
        if position.x - 1 >= 0 {
            map[position.x - 1][position.y] = dice.move(op, map[position.x - 1][position.y])
            position.x -= 1
        }
    case 4:
        if position.x + 1 < mapSize.M {
            map[position.x + 1][position.y] = dice.move(op, map[position.x + 1][position.y])
            position.x += 1
        }
    default:
        break
    }
}

class Dice {
/*
        up
 left, top, right
       down
      bottom
*/
    var top = 0
    var left = 0
    var right = 0
    var up = 0
    var bottom = 0
    var down = 0

    func move(_ order: Int, _ cell: Int) -> Int {

        let temp = (top: top, left: left, right: right, bottom: bottom, down: down, up: up)

        switch order {
            // 동
        case 1:
            top = temp.left
            left = temp.bottom
            right = temp.top
            bottom = temp.right
            // 서
        case 2:
            top = temp.right
            left = temp.top
            right = temp.bottom
            bottom = temp.left
            // 북
        case 3:
            up = temp.top
            top = temp.down
            down = temp.bottom
            bottom = temp.up
            // 남
        case 4:
            up = temp.bottom
            top = temp.up
            down = temp.top
            bottom = temp.down

        default:
            return cell
        }

        print(top)

        if cell == 0 {
            return self.bottom
        } else {
            bottom = cell
            return 0
        }
    }
}
