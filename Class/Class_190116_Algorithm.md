# 알고리즘 개관

#### 2019-01-16



#### Language 구성

- type
- 제어
  - 순차구조
  - 선택구조
  - 반복구조



#### 자료구조

- 자료구조
  - 선형 자료구조
    - 배열, 리스트, 스택, 큐, 문자열
  - 비선형 자료구조
    - 트리 (1차 배열, 링크드 리스트)
    - 그래프 (인접 행렬, 인접 리스트)
- 연산
  - 삽입, 삭제



#### 알고리즘

- 그리드, 탐욕 알고리즘 설계 기법
- 분할 정복
- 백트랭킹 (상태공간 트리 + DFS, 가지치기)
- DP 다이나믹 프로그래밍, 동적 계획법
  - 재귀적 DP
  - 반복적 DP



#### 배열

같은 타입의 요소를 묶어서 다니는 것



#### 완전 검색

Brute-force 컴퓨터는 1초에 1억번 정도 카운팅 할 수 있다. generate-and-test라고도 한다. 모든 예를 다 생성해서 다 조사하는 것이다.



#### 탐욕 알고리즘

1. 로컬로 선택
2. 이 상태에서 맞는지 안 맞는지만 확인
3. 검사 통과한 답을 모아서 전체 해를 검사

=> 왠만하면 쓰지 말 것. 완전 검색을 쓸 것



#### 버블 정렬

인접한 두 개의 원소를 비교하여 자리를 계속 교환하는 방식

for문이 뒤에까지 돌고, 맨 뒤에 정렬되면 그 앞까지 돌고, 하니까 5+4+3+2+1 이런식으로 들어가기 때문에 n(n+1) /2 = n^2/2 + n/2니까 시간 복잡도는 n^2이다.



#### 카운팅 정렬

n의 길이에 depend되고, 버블 정렬과 달리 한 번 쭉 훑으면 끝난다. 정수류여야하고, 범위가 정해져있어야 카운팅 정렬을 할 수 있다. 





