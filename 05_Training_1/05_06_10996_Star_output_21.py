"""
문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 차례대로 별을 출력한다.

예제 입력 1
1
예제 출력 1
*

예제 입력 2
2
예제 출력 2
*
 *
*
 *

예제 입력 3
3
예제 출력 3
* *
 *
* *
 *
* *
 *

예제 입력 4
4
예제 출력 4
* *
 * *
* *
 * *
* *
 * *
* *
 * *
"""


def main():
    star_count = int(input())

    for i in range(star_count*2):
        for j in range(star_count):
            if i % 2 == 0:
                if j % 2 == 0:
                    print("*", end='')
                elif j % 2 == 1:
                    print(" ", end='')
            elif i % 2 == 1:
                if j % 2 == 1:
                    print("*", end='')
                elif j % 2 == 0:
                    print(" ", end='')
        print()


if __name__ == '__main__':
    main()
