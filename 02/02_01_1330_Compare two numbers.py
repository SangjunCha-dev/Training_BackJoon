"""
문제
두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

입력
첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.

출력
첫째 줄에 다음 세 가지 중 하나를 출력한다.

A가 B보다 큰 경우에는 '>'를 출력한다.
A가 B보다 작은 경우에는 '<'를 출력한다.
A와 B가 같은 경우에는 '=='를 출력한다.
제한
-10,000 ≤ A, B ≤ 10,000
예제 입력 1
1 2
예제 출력 1
<

예제 입력 2
10 2
예제 출력 2
>

예제 입력 3
5 5
예제 출력 3
==
"""


def main():
    num_list = list(map(int, input().split()))

    num_max = max(num_list)
    num_min = min(num_list)

    if num_min < -10000 or 10000 < num_max:
        return

    compare_result = ''
    if num_list[0] < num_list[1]:
        compare_result = '<'
    elif num_list[0] > num_list[1]:
        compare_result = '>'
    elif num_list[0] == num_list[1]:
        compare_result = '=='

    print(compare_result)


if __name__ == '__main__':
    main()
