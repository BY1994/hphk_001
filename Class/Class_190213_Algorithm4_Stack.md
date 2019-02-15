# 알고리즘 - 스택

2019-02-13



### 스택

- 재귀호출
- Memoization
- DP
- DFS



### 스택의 구현

공백 스택에서 바닥을 가리키고 있따가, 하나씩 위로 쌓아올라가면서 한 칸 위를 카리킨다. 스택이 가득차면 stack overflow가 일어나고, 스택에서 하나씩 꺼내다가 더 이상 꺼낼 게 없으면 undeflow가 일어난다.

```python
stack = [0] * 10
top = -1

for i in range(3):
	stack[top+1] = i # 탑 위치 위에다가 값을 저장하고
	top += 1 # 탑을 증가시킨다.

for i in range(3): # 3개 있다는 걸 확실히 아니까 언더플로 처리를 또 따로 써주지는 않았다
	t = stack[top]; top -= 1
	print(t) # 0, 1, 2가 들어와서 2, 1, 0으로 결과값이 나오게 될 것이다.
```

_사용자 정의 스택에 해당한다_



### 재귀함수

함수의 정의 안에 자기 자신이 정의되어있으면 재귀호출이다. base part와 inductive part (유도 파트)가 있다. 함수 호출이 무한히 되면 stack overflow가 나기 때문에 base part로 정의역을 지정해주어야한다. 

_시스템 스택에 해당한다_



### 메모이제이션

기록하다에 어원이 있는데, 했던 일을 기록해서 그걸 참고해서 또 하는 일이 없도록 하겠다는 것이다. 재귀함수를 발전시키되, 기록을 활용하여 돌았던 재귀함수를 다시 돌지 않게 한다.

```python
# 전역에 메모라고 하나 둔다.
memo = [0] * 100
# 이니셜값으로 베이스 케이스는 줘야할 것이다.
memo[0] = 0
memo[1] = 1

def f(n):
	if n<2 or memo[n] != 0: return memo[n]
	memo[m] =  f(n-1) + f(n-2) # 이 결과값을 저장
	return memo[m]
```



### DP

재귀가 아닌 반복구조로 표현하면 DP가 된다. 작은 범위의 해들을 이용해서 보다 큰 범위의 해를 구해나가는 방법이기도 하다. 

```python
s[0] = 0
s[1] = 1
# solution 공간의 0과 1은 위와 같이 정해준다.
for i in range(2, n+1):
	s[i] = s[i-1] + s[i-2]
# 선형으로 반복문 한 번 쓰면 끝난다.
```



fibo()       ------>     fiboMemo()       --------> fiboIter()

재귀                       memo, 재귀                    DP



### 비선형 자료구조

선형 자료구조에는 기본적인 배열, 스택, 큐, 리스트 정도가 있다. 엘리먼트들의 관계가 1대 1이다. 비선형 자료구조는 엘리먼트와 엘리먼트의 관계가 1대 다이다. 그래프와 트리가 있다.

- 그래프
  - 표현
    - 인접행렬
    - 인접리스트
  - 순회
    - DFS (사용자 정의 스택, 시스템 스택(재귀))
    - BFS (큐)
- 트리
  - 표현
    - 인접행렬
    - 인접리스트
  - 순회
    - inorder 순회
    - postorder 순회
    - preorder 순회



### DFS

1) 어떤 시작 정점 v를 결정하여 방문한다. 

그 노드의 데이터값을 화면에 출력하는 것으로 연습을 한다. 필요하면 백트랙킹 계산을 넣을 것이다.

2) 정점 v에 인접한 정점 중에서 (adjacent, connect가 아니라 다 이렇게 쓴다 인접 행렬 adjacent matrix)

1 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문한다. 그리고 w를 v로 하여 다시 2)를 반복한다.

2 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2)를 반복한다.

3) 스택이 공백이 될 때까지 2)를 반복한다.