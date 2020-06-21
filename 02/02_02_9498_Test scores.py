"""
문제
시험 점수를 입력받아 출력하는 프로그램을 작성하시오.
90 ~ 100점은 A,
80 ~ 89점은 B,
70 ~ 79점은 C,
60 ~ 69점은 D,
나머지 점수는 F

입력
첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
시험 성적을 출력한다.

예제 입력 1
100
예제 출력 1
A
"""


def main():
    score = int(input())

    if score < 0 or 100 < score:
        return

    score_result = ''
    if 90 <= score:
        score_result = 'A'
    elif 80 <= score:
        score_result = 'B'
    elif 70 <= score:
        score_result = 'C'
    elif 60 <= score:
        score_result = 'D'
    else:
        score_result = 'F'

    print(score_result)


if __name__ == '__main__':
    main()
