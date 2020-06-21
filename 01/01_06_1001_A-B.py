"""
문제
두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
첫째 줄에 A-B를 출력한다.

예제 입력 1
3 2

예제 출력 1
1
"""


def main():
    num_list = list(map(int, input().split()))

    num_min = min(num_list)
    num_max = max(num_list)
    if num_min < 1 or 9 < num_max:
        return

    result = num_list[0] - num_list[1]
    print(result)


if __name__ == '__main__':
    main()