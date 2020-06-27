"""
문제
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

입력
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

예제 입력 1
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
예제 출력 1
40.000%
57.143%
33.333%
66.667%
55.556%
"""
import sys


def main():
    test_case = int(sys.stdin.readline())
    test_list = [list(map(int, sys.stdin.readline().split())) for _ in range(test_case)]
    score_avg = [0 for _ in range(test_case)]
    above_average = [0 for _ in range(test_case)]

    students_list = [int(test_list[i].pop(0)) for i in range(test_case)]

    for i in range(test_case):
        score_avg[i] = sum(test_list[i]) / students_list[i]
        above_score_count = 0

        for j in range(students_list[i]):
            if score_avg[i] < test_list[i][j]:
                above_score_count += 1

        above_average[i] = above_score_count / students_list[i] * 100

    [print("{0:.3f}%".format(above_average[i])) for i in range(test_case)]


if __name__ == '__main__':
    main()
