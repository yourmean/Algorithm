## 자료구조 기초 

탐색 : 원하는 데이터를 찾는 과정

자료구조: 데이터를 표현/관리/처리하기 위한 구조

    스택/큐 -> 삽입/삭제 고려, (언더/오버플로 고려도 need)

---

### 스택
박스 쌓기 - 선입후출(후입선출) 구조

입구& 출구가 동일한 형태

스택 예제
``` python
stack= []

stack.append(5) #삽입
stack.pop() #삭제

print(stack) #최하단 원소부터
print(stack[::-1]) #최상단 원소부터
```

---

### 큐
대기줄 - 선입선출 구조 (공정한 자료구조)

큐 예제
``` python
from collections import deque

queue= deque()

queue.append(5)
queue.append(3)
queue.popleft()

print(queue) #먼저 들어온 원소부터
queue.reverse() #다음 출력을 위한 역순 처리
print(queue) #나중에 들어온 원소부터 
list(queue) #deque 객체를 list 자료형 반환
```

---

### 재귀 함수

- 재귀 함수의 종료 조건
    : if문으로


팩토리얼 함수 구현 (재귀적 vs. 반복적)
``` python
# 1. 반복적
def frac1(n):
    result=1
    for i in range(1,n+1):
        result+=i
    return result

# 2. 재귀적 - 종료 조건 n<=1
def frac2(n):
    if n<=1:
        return 1
    return n*frac2(n-1)
```

## 탐색 알고리즘 DFS/BFS

`
### DFS (Depth-First Search)
깊이 우선 탐색 - 그래프에서 깊은 부분을 우선적으로 탐색

### Graph
구성
- node(vertex) : 도시
- edge : 도로

그래프 탐색
    : 하나의 노드를 시작으로 다수의 노드를 방문하는 것

그래프 표현
1. 인접 행렬(adjacency matrix) 방식
    : 2차원 배열에 노드가 연결된 형태 기록
    : 연결 X - 무한
2. 인접 리스트(adjacency list) 방식
    : 모든 노드에 연결된 노드에 대한 정보를 차례로 연결하여 저장
`
