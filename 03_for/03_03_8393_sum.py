"""
문제
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

출력
1부터 n까지 합을 출력한다.

예제 입력 1
3

예제 출력 1
6
"""


def main():
    number = int(input())

    if number < 1 or 10000 < number:
        return

    num_sum = 0
    # for i in range(1, number+1):
    #     num_sum += i
    #
    # print(num_sum)

    num_sum = int((number * (number+1))/2)
    print(num_sum)


if __name__ == '__main__':
    main()
