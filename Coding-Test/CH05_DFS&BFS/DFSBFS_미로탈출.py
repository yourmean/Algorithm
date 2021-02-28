from collections import deque

n,m= map(int, input().split())
board=[list(map(int, input())) for _ in range(n)]

# 방향
dx= [0, 0, -1, 1]
dy= [1, -1, 0, 0]

def bfs(x,y):
    q= deque()
    q.append((x,y))

    while q:
        x,y= q.popleft()
        for i in range(4):
            nx= x+ dx[i]
            ny= y+ dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m or board[nx][ny]==0:
                continue

            if board[nx][ny]==1:
                board[nx][ny]= board[x][y]+1
                q.append((x,y))
    return board[n-1][m-1]
print(bfs(0,0))

