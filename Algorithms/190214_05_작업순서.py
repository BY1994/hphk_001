"""
[S/W 문제해결 응용] 10일차 - 작업순서
문제 내용
해야 할 V개의 작업이 있다. 이들 중에 어떤 작업은 특정 작업이 끝나야 시작할 수 있으며, 이를 선행 관계라 하자.
이런 작업의 선행 관계를 나타낸 그래프가 주어진다.
이 그래프에서 각 작업은 하나씩의 정점으로 표시되고 선행 관계는 방향성을 가진 간선으로 표현된다.
단, 이 그래프에서 사이클은 존재하지 않는다 (사이클은 한 정점에서 시작해서 같은 정점으로 돌아오는 경로를 말한다).
이 그래프에서 작업 1은 작업 4가 끝나야 시작할 수 있다.
작업 6은 작업 5와 작업 7이 끝나야 할 수 있다.
이 그래프에서는 사이클이 없다.
김과장은 선행 관계가 주어진 작업군을 한 번에 하나의 작업씩 처리해서 다 끝내려 한다.
위에서 예를 든 작업군에 대해서 이런 일을 한다면 아래의 순서로 처리할 수 있다.
8, 9, 4, 1, 5, 2, 3, 7, 6
또한 아래의 순서도 가능하다.
4, 1, 2, 3, 8, 5, 7, 6, 9
아래의 순서는 가능하지 않다.
4, 1, 5, 2, 3, 7, 6, 8, 9
이 순서에서는 작업 5가 작업 8보다 먼저 처리되는데, 위 그래프에서 주어진 선행 관계에서는 작업 5는 작업 8이 끝나야 시작할 수 있어 이 순서로 끝내는 것은 가능하지 않다.
V개의 작업과 이들 간의 선행 관계가 주어질 때, 한 사람이 한 번에 하나씩 일을 할 수 있는 작업 순서를 찾는 프로그램을 작성하라.
가능한 작업 순서는 보통 여러 가지가 있으므로 여러분은 이들 중 하나만 제시하면 된다.
사이클이 있는 그래프는 입력에서 주어지지 않으므로 이런 경우에 대한 에러 처리는 고려하지 않아도 좋다.
사이클이 없는 그래프에서 가능한 순서는 항상 존재한다.

[입력]
10개의 테스트 케이스가 주어진다.
20줄에 걸쳐, 두 줄에 테스트 케이스 하나씩 제공된다.
각 케이스의 첫줄에는 그래프의 정점의 총 수 V와 간선의 총 수 E가 주어진다.
그 다음 줄에는 E개 간선이 나열된다.
간선은 간선을 이루는 두 정점으로 표기된다.
예를 들어, 정점 5에서 28로 연결되는 간선은 “5 28”로 표기된다.
정점의 번호는 1부터 V까지의 정수값을 가지며, 입력에서 이웃한 수는 모두 공백으로 구분된다.

[출력]
총 10줄에 10개의 테스트케이스 각각에 대한 답을 출력한다.
각 줄은 ‘#x’로 시작하고 공백을 하나 둔 다음 작업 순서를 기록한다.
작업 순서는 V개 정수를 공백을 사이에 두고 나열하는 것이다.

최초 작성 2019.02.14 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190214_05_input.txt", "r")

for tc in range(10):

    # input
    V, E = map(int, input().split())
    lines = list(map(int, input().split()))

    # output
    print("#{} ".format(tc + 1), end='')

    # 그래프 행렬 채우기
    G = [[0 for _ in range(V+1)] for __ in range(V)]

    for idx in range(0, len(lines), 2):
        G[lines[idx]-1][lines[idx+1]-1] = 1 # 연결된 것 표시
        G[lines[idx+1]-1][-1] += 1 # 진입 차수 증가

    # 진입차수 0인 것 지우기
    while E: # 모든 간선을 지울 때까지
        for node in range(V):
            if G[node][-1] == 0: # 그러면 0된 애 또 만나는데
                print(node+1, end=' ') # 지우는 간선 print
                G[node][-1] = -100 # 다시 안 돌도록 들어오면 체크
                # 연결된 애들의 간선을 모두 지워줌
                for i in range(V):
                    if G[node][i] == 1:
                        G[i][-1] -= 1
                        E -= 1
                break
    # 마지막 노드
    for node in range(V):
        if G[node][-1] == 0:  # 그러면 0된 애 또 만나는데
            print(node + 1, end=' ')  # 지우는 간선 print

    print()
