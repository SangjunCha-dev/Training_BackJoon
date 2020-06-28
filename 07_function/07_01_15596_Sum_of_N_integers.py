"""
문제
정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.

작성해야 하는 함수는 다음과 같다.

def solve(a: list) -> int
a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
리턴값: a에 포함되어 있는 정수 n개의 합 (정수)
"""
import sys


def solve(a: list):  # 212ms
    num_sum = 0
    for i in range(len(a)):
        num_sum += a[i]

    return int(num_sum)


def solve2(a):  # 28ms
    return sum(a)


if __name__ == '__main__':
    num_list = list(map(int, sys.stdin.readline().split()))

    print(solve(num_list))
