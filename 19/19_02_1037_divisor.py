"""
문제
양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다.
어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N의 진짜 약수의 개수가 주어진다. 이 개수는 50보다 작거나 같은 자연수이다.
둘째 줄에는 N의 진짜 약수가 주어진다.
1,000,000보다 작거나 같고, 2보다 크거나 같은 자연수이고, 중복되지 않는다.

출력
첫째 줄에 N을 출력한다. N은 항상 32비트 부호있는 정수로 표현할 수 있다.

예제 입력 1
2
4 2

예제 출력 1
8
"""

"""
첫번째 입력 - 약수의 개수(50보다 작거나 같은 자연수)
두번째 입력 - 약수 입력

출력 - N 출력
"""


def main():
    num1 = int(input())
    num2 = list(map(int, input().split()))

    # 또는 아래 방식으로 형변환
    # num2 = map(int, input().split())
    # num2 = [int(i) for i in num2]

    numMax = max(num2)
    numMin = min(num2)
    numCount = len(num2)

    if num1 < 1 or 50 < num1:
        return
    if numMin < 2 or 1000000 < numMax:
        return
    if not num1 == numCount:
        return

    divisor = numMin * numMax
    print(divisor)


if __name__ == '__main__':
    main()
