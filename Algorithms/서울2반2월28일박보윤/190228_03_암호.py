"""
5120. [파이썬 S/W 문제해결 기본] 7일차 - 암호
문제 내용
A사는 창립기념일 이벤트로 비밀번호 맞추기 대회를 열어, 최대 10개인 비밀번호를 맞추는 사람에게 기념품을 제공하기로 했다.
기념품을 받을 수 있도록 다음 조건에 맞는 비밀번호 찾기 프로그램을 작성하시오.
- 1000이하의 숫자 N개가 주어진다. 이때 시작 숫자가 정해지고, 첫 번째 지정 위치가 된다.
- 지정 위치부터 M번째 칸을 추가한다. 여기에 앞칸의 숫자와 뒤로 밀려난 칸의 숫자를 더해 넣는다. 추가된 칸이 새로운 지정 위치가 된다. 밀려난 칸이 없으면 시작 숫자와 더한다.
- 이 작업을 K회 반복하는데, M칸 전에 마지막 숫자에 이르면 남은 칸수는 시작 숫자부터 이어간다.
- 마지막 숫자부터 역순으로 숫자를 출력하면 비밀번호가 된다. 숫자가 10개 이상인 경우 10개까지만 출력한다.
다음은 N, M, K가 6, 3, 3이고, 주어진 숫자가 6, 2, 4, 9, 1, 5인 경우의 예이다. 6이 시작 숫자이자 첫번째 지정 위치가 된다.
(1) 3번째에 새로운 칸을 추가하고, 앞의 숫자 4와 뒤로 밀려난 9를 더해 칸을 채운다.
(2) 다시 3칸 뒤에 새로운 칸을 추가하고, 앞 뒤 숫자를 더해 넣는다.
(3) 다시 3칸 뒤에 칸을 추가하고 앞 뒤 숫자를 더해 넣는다.
암호는 역순인 5 6 1 9 13 4 2 8 6이 된다.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 첫 줄에 N, M, K가, 다음 줄에 1000이하의 자연수 N개가 주어진다. 3<=N, M, K<=1000

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

최초 작성 2019.02.27 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190228_03_input.txt", "r")

T = int(input())

for tc in range(T):
    # input
    N, M, K = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    idx = 0
    for _ in range(K): # K회 반복
        idx += M

        if idx > len(numbers):
            idx -= len(numbers)

        if idx == 0 or idx == len(numbers): # 맨 앞이나 맨 뒤인 경우 이전 값과 다음 값 처리를 따로 해주었다.
            numbers.insert(idx, numbers[-1] + numbers[0])
            continue

        numbers.insert(idx, numbers[idx-1] + numbers[idx]) # 합한 값을 넣는다.

    print("#%d %s" %(tc+1, ' '.join(list(map(str,numbers[::-1][:10])))))


"""    
1. 단순히 모듈라 연산으로 하면 풀린다고 생각했는데, 잘못된 인덱스로 자꾸 갔다...
그래서 - length 로 바꿨다.

2. idx == 0 인 경우와 idx == 마지막 인 경우를 따로 처리해주었다.
특히 마지막 인덱스를 처리 안해주면 잘못된 위치에 들어간다.

3. 엄청난 바보였다!!!!!!!!!! M자리에 3을 써놓고 왜 3번째 케이스가 틀린지 고민했다!!!!!!
"""