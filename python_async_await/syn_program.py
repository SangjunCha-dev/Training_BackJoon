"""
실습 프로젝트
지금부터 사용자 관리 애플리케이션을 흉내내는 실습 코드를 작성하면서 동기 처리하는 코드와 비동기 처리를 하는 코드를 비교해보도록 하겠습니다.

억지스럽지만 시뮬레이션을 위해서 다음과 같은 가정을 해보겠습니다.

애플리케이션을 사용자 데이터를 직접 보관하지 않고 외부 API를 호출해서 가져옵니다.
외부 API는 1명의 사용자 데이터를 조회하는데 1초가 걸리고, 한 번에 여러 사용자의 데이터를 조회할 수 없습니다.
각각 3명, 2명, 1명의 사용자 정보를 조회하는 요청 3개가 동시에 애플리케이션에 들어옵니다.
"""
import time


def find_users_sync(n):
    """
    사용자 데이터 조회를 전통적인 동기 방식으로 처리
    의도적으로 1초의 지연 시간을 발생
    :param n:
    :return:
    """
    for i in range(1, n+1):
        print("{0}명 중 {1}번 째 사용자 조회 중 ...".format(n, i))
        time.sleep(1)
    print("> 총 {0} 명 사용자 동기 조회 완료!".format(n))


def process_sync():
    start = time.time()
    find_users_sync(3)
    find_users_sync(2)
    find_users_sync(1)
    end = time.time()
    print(">>> 동기 처리 총 소요 시간: {0}".format(end - start))


def main():
    process_sync()


if __name__ == '__main__':
    main()
