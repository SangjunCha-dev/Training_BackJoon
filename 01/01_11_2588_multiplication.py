"""
문제
(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
      4 7 2 --- (1)
    x 3 8 5 --- (2)
------------
    2 3 6 0 --- (3)
  3 7 7 6   --- (4)
1 4 1 6     --- (5)
------------
1 8 1 7 2 0 --- (6)

(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때
(3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

출력
첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

예제 입력 1
472
385

예제 출력 1
2360
3776
1416
181720
"""


def main():
    num_list1 = int(input())
    num_list2 = int(input())

    num_max = max(num_list1, num_list2)

    if 999 < num_max:
        return

    num_rem100 = int(num_list2 / 100)
    num_rem1 = num_list2 % 10
    num_rem10 = int((num_list2 - num_rem100*100 - num_rem1) / 10)

    num_mul1 = num_list1 * num_rem1
    print(num_mul1)
    num_mul2 = num_list1 * num_rem10
    print(num_mul2)
    num_mul3 = num_list1 * num_rem100
    print(num_mul3)
    num_mul4 = num_list1 * num_list2
    print(num_mul4)


if __name__ == '__main__':
    main()
