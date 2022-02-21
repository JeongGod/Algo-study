//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/02/15.
// 2020 KAKAO BLIND RECRUITMENT > 기둥과 보 설치 > 60061

import Foundation

// a = 0 기둥 / a = 1 보
// map[x][y][a] == 0 or 1
var map = [[[Int]]]()

func pilar(to frame: [Int]) {

    let x = frame[0]
    let y = frame[1]
    let a = frame[2] // 기둥(0), 보(1)
    let b = frame[3] // 삭제(0) , 설치(1)

    if b == 0 {
        // 삭제
        if a == 0 {
            // 기둥 삭제

            // 삭제 될 기둥 끝에 기둥이 있을 때,
            if y + 1 <= map.count, map[x][y + 1][0] == 1 {
                guard (x - 1 >= 0 && map[x - 1][y + 1][1] == 1) || map[x][y + 1][1] == 1 else { return }
            }
            // 삭제 될 기둥 끝에 보가 있을 때,
            if y + 1 <= map.count, map[x][y + 1][1] == 1 {
                guard
                (x + 1 <= map.count && map[x + 1][y][0] == 1) ||
                    ((x - 1 >= 0 && map[x - 1][y + 1][1] == 1) && (x + 1 <= map.count && map[x + 1][y + 1][1] == 1))
                    else {
                    return
                }
            }
            if y + 1 <= map.count, x - 1 >= 0, map[x - 1][y + 1][1] == 1 {
                guard
                (x - 1 >= 0 && map[x - 1][y][0] == 1) ||
                    ((x - 2 >= 0 && map[x - 2][y + 1][1] == 1) && map[x][y + 1][1] == 1)
                    else {
                    return
                }
            }
            map[x][y][a] = 0

        } else {
            // 보 삭제

            // 보 끝에 기둥이 있을 때
            if x + 1 <= map.count, map[x + 1][y][0] == 1 {
                guard (y - 1 >= 0 && map[x + 1][y - 1][0] == 1) || map[x + 1][y][1] == 1 else { return }
            }

            if map[x][y][0] == 1 {
                guard
                (y - 1 >= 0 && map[x][y - 1][0] == 1) ||
                    (x - 1 >= 0 && map[x - 1][y][1] == 1)
                    else {
                    return
                }
            }

            // 보 끝에 보가 있을 때
            if x + 1 <= map.count, map[x + 1][y][1] == 1 {
                guard
                (x + 1 <= map.count && y - 1 >= 0 && map[x + 1][y - 1][0] == 1) ||
                    (x + 2 <= map.count && y - 1 >= 0 && map[x + 2][y - 1][0] == 1)
                    else {
                    return
                }
            }

            if x - 1 >= 0, map[x - 1][y][1] == 1 {
                guard
                (y - 1 >= 0 && map[x - 1][y - 1][0] == 1) ||
                    (y - 1 >= 0 && map[x][y - 1][0] == 1)
                    else {
                    return
                }
            }
            map[x][y][a] = 0
        }

    } else {
        // 설치
        if a == 0 {
            guard
            y == 0 ||
                map[x][y][1] == 1 ||
                (x - 1 >= 0 && map[x - 1][y][1] == 1) ||
                (y - 1 >= 0 && map[x][y - 1][0] == 1)
                else {
                return
            }
            map[x][y][a] = 1
        } else {
            guard
            map[x][y - 1][0] == 1 ||
                (x + 1 <= map.count && y - 1 >= 0 && map[x + 1][y - 1][0] == 1) ||
                (x - 1 >= 0 && x + 1 <= map.count && map[x - 1][y][1] == 1 && map[x + 1][y][1] == 1)
                else {
                return
            }
            map[x][y][a] = 1
        }
    }
}

func solution(_ n: Int, _ build_frame: [[Int]]) -> [[Int]] {

    map = [[[Int]]](repeating: [[Int]](repeating: [Int](repeating: 0, count: 2), count: n + 1), count: n + 1)

    for frame in build_frame {
        pilar(to: frame)

    }

    var result = [[Int]]()

    for (i, m1) in map.enumerated() {
        for (j, m2) in m1.enumerated() {
            for (k, a) in m2.enumerated() {
                if a == 1 {
                    result.append([i, j, k])
                }
            }
        }
    }

    return result
}

