'''
N*N 정사각형 공간, (1,1)에서 출발하여 L R U D 방향으로 한 칸씩 이동할 때,
최종 지점의 x,y좌표를 공백으로 구부낳여 출력
이 때, 정사각형 공간을 벗어나는 움직임은 무시
'''

def solution():
    n= int(input()) #정사각형 크기
    plan= input().split() #주어진 움직임, input().split() 도 무방

    x,y= 1,1 #출발지점
    dx= [0,0,-1,1]
    dy= [-1,1,0,0]
    type= ['L', 'R', 'U', 'D']
    
    for p in plan:
        for i in range(len(type)):
            if plan==type[i]:
                nx= x+dx[i]
                ny= y+dy[i]
            if nx<1 or nx>n or ny<1 or ny>n:
                continue
            x,y= nx, ny

    print (x,y)

solution()