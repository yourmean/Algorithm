# failed - 방문 여부 판단 X, 끝없이 돌아가는 코드,,

def solution():
    h,w= map(int, input().split())
    x, y, d= map(int, input().split())

    map= []
    for i in range(h):
        map.append(list(map(int, input.split())))

    # 북서남동
    dx= [-1,0,1,0]
    dy= [0,-1,0,1] # 왼쪽으로 회전 dxdy[(i+1)%4]

    # 수행해보자
    answer= 1
    turn= 0
    while True:
        # 방향 회전
        d= (d+1)%4

        # 방문한 적 없고, 육지면 한 칸 이동
        if map[x+dx[d]][y+dy[d]]==0:
            x += dx[d]
            y += dy[d]
            answer+= 1
            turn= 0

        # 갈 수 없는 경우
        else:
            turn+= 1
        if turn==4:
            if map[x-dx[d]][y-dy[d]] == 0:
                x -= dx[d]
                y -= dy[d]
            else:
                break
            turn= 0
    return answer
solution()