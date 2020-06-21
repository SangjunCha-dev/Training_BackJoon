"""
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 A+B를 출력한다.

예제 입력 1
5
1 1
2 3
3 4
9 8
5 2

예제 출력 1
2
5
7
17
7
"""


def main():
    case_count = int(input())
    num_list = []

    for i in range(0, case_count):
        number = list(map(int, input().split()))
        num_list.append(number)

        if num_list[i][0] <= 0 or 10 <= num_list[i][0]:
            return
        elif num_list[i][1] <= 0 or 10 <= num_list[i][1]:
            return

    for i in range(0, case_count):
        num_sum = num_list[i][0] + num_list[i][1]
        print(num_sum)


if __name__ == '__main__':
    main()
