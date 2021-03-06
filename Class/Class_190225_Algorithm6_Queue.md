# 큐 (Queue)

2019-02-25



### 목차

- 큐
- 우선순위 큐
- BFS
- 큐의 활용: 버퍼
- 최단경로



### 큐

스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조

선입 선출 구조(FIFO, First In First Out) -> 줄을 서서 버스를 타는 경우를 생각하면 된다. 먼저 줄을 선 사람이 먼저 나가게 된다.

큐의 기본 연산 중 삽입은 enQueue, 삭제는 deQueue라고 부른다.



### 선형 큐 이용시의 문제점

선형 큐를 사용할 경우 인덱스를 계속 뒤로 밀면서 진행하기 때문에 포화상태로 잘못 인식하고 끝나는 경우가 생길 수 있다.  이를 해결하기 위해서 1) 매 연산이 이루어질 때마다 저장된 원소들을 배열의 앞부분으로 모두 이동시키거나 2) 큐의 인덱스를 모듈라 연산(%) 을 통해서 다시 앞에서부터 인덱스를 채워나가게 하는 원형 큐를 사용한다. 3) 혹은 Linked List를 사용하여 연결 큐를 만들 수도 있다.



### 우선순위 큐 (Priority Queue)

우선순위를 가진 항목들을 저장하는 방식이고, FIFO 순서가 아니라 우선순위가 높은 순서대로 먼저 나가게 된다. 뒤에서부터 확인하면서 내 숫자보다 큰지 작은지 보면서 나보다 크면 뒤로 한칸씩 밀어서 내 자리를 찾을 때까지 민다. 숫자가 매우 크고 정렬되어있는 경우에 0이 들어오면 링크드 리스트보다 훨씬 오래걸릴 수 있다.



### 큐의 활용: 버퍼 (Buffer)

버퍼란 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역을 뜻한다. 버퍼는 순서대로 입력/출력/전달되어야 하므로 FIFO 방식의 자료구조인 큐가 활용된다. 



### BFS (Breadth First Search)

그래프를 탐색하는 방법 (순회하는 방법)에는 크게 두 가지가 있다. DFS와 BFS이다.  자기 자신을 처리하고 그 다음에 이웃 정점들을 큐에 넣는 것을 반복한다.