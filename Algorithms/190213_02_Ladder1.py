"""
[S/W 문제해결 기본] 2일차 - Ladder1
문제 내용
점심 시간에 산책을 다니는 사원들은 최근 날씨가 더워져, 사다리 게임을 통하여 누가 아이스크림을 구입할지 결정하기로 한다.
김 대리는 사다리타기에 참여하지 않는 대신 사다리를 그리기로 하였다.
사다리를 다 그리고 보니 김 대리는 어느 사다리를 고르면 X표시에 도착하게 되는지 궁금해졌다. 이를 구해보자.
아래 <그림 1>의 예를 살펴보면, 출발점 x=0 및 x=9인 세로 방향의 두 막대 사이에 임의의 개수의 막대들이 랜덤 간격으로 추가되고(이 예에서는 2개가 추가됨) 이 막대들 사이에 가로 방향의 선들이 또한 랜덤하게 연결된다.
X=0인 출발점에서 출발하는 사례에 대해서 화살표로 표시한 바와 같이, 아래 방향으로 진행하면서 좌우 방향으로 이동 가능한 통로가 나타나면 방향 전환을 하게 된다.
방향 전환 이후엔 다시 아래 방향으로만 이동하게 되며, 바닥에 도착하면 멈추게 된다.
문제의 X표시에 도착하려면 X=4인 출발점에서 출발해야 하므로 답은 4가 된다. 해당 경로는 별도로 표시하였다.
아래 <그림 2>와 같은 100 x 100 크기의 2차원 배열로 주어진 사다리에 대해서, 지정된 도착점에 대응되는 출발점 X를 반환하는 코드를 작성하라 (‘0’으로 채워진 평면상에 사다리는 연속된 ‘1’로 표현된다. 도착 지점은 '2'로 표현된다).

[입력]
입력 파일의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.
총 10개의 테스트 케이스가 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도착하게 되는 출발점의 x좌표를 출력한다.

최초 작성 2019.02.13 PBY
"""
# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190213_02_input.txt", "r")

for tc in range(10):

    # input
    tnum = input()
    ladder = []
    for _ in range(100):
        ladder.append(input().split())

    # 2가 있는 위치 찾기
    for _ in range(100):
        if ladder[-1][_] == '2':
            location = _

    # 2가 있는 위치에서 올라가기
    for _ in range(100-1, -1, -1):
        if location >= 1 and ladder[_][location-1] == '1': # 왼쪽
            location -= 1
            for j in range(location-1, -1, -1):
                if ladder[_][j] == '0':
                    break
                location -= 1

        elif location <= 98 and ladder[_][location+1] == '1': # 오른쪽
            location += 1
            for j in range(location+1, 100):
                if ladder[_][j] == '0':
                    break
                location += 1

    print("#{} {}".format(tc+1, location))