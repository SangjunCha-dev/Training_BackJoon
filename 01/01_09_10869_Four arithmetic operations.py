"""
문제
두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.

입력
두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

출력
첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

예제 입력 1
7 3

예제 출력 1
10
4
21
2
1
"""


def main():
    num_list = list(map(int, input().split()))

    num_max = max(num_list)
    num_min = min(num_list)

    if num_min < 1 or 10000 < num_max:
        return

    num_sum = num_list[0] + num_list[1]
    print(num_sum)

    num_sub = num_list[0] - num_list[1]
    print(num_sub)

    num_mul = num_list[0] * num_list[1]
    print(num_mul)

    num_div = int(num_list[0] / num_list[1])
    print(num_div)

    num_rem = num_list[0] % num_list[1]
    print(num_rem)


if __name__ == '__main__':
    main()