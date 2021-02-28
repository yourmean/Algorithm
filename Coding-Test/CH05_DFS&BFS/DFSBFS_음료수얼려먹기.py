n,m= map(int, input().split())

board= []
for i in range(n):
    board.append(list(map(int, input())))
    board= [list(map(int, input())) for _ in range(n)]

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return 0
    if board[x][y]==0:
        board[x][y]= 1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return 1
    return 0

answer= 0
for x in range(n):
    for y in range(m):
        if dfs(x,y)==1:
            answer+=1

print(result)