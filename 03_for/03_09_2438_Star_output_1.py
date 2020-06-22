"""
문제
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

예제 입력 1
5

예제 출력 1
*
**
***
****
*****
"""


def main():
    number = int(input())

    if number < 1 or 100 < number:
        return

    for i in range(1, number+1):
        for j in range(i):
            print("*", end='')
        print("")


if __name__ == '__main__':
    main()
