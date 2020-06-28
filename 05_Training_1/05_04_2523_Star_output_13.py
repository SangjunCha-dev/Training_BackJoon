"""
문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

예제 입력 1
3

예제 출력 1
*
**
***
**
*
"""


def main():
    star_count = int(input())

    for i in range(1, star_count+1):
        for j in range(i):
            print("*", end='')
        print()

    for i in range(star_count, 0, -1):
        for j in range(i-1):
            print("*", end='')
        print()


if __name__ == '__main__':
    main()
