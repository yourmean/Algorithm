'''
N*N 정사각형 공간, (1,1)에서 출발하여 L R U D 방향으로 한 칸씩 이동할 때,
최종 지점의 x,y좌표를 공백으로 구부낳여 출력
이 때, 정사각형 공간을 벗어나는 움직임은 무시
'''

def solution():
    n= int(input()) #정사각형 크기
    move= list(map(str, input().split())) #주어진 움직임, input().split() 도 무방

    p= [1, 1] #출발지점
    for m in move:
        if m=='L':
            p[1]-=1 if p[1]-1>0 else 0
        elif m == 'R':
            p[1] += 1 if p[1]+1 < n+1  else 0
        elif m == 'U':
            p[0] -= 1 if p[0]-1 > 0  else 0
        else: #m == 'R'
            p[0] += 1 if p[0]+1 < n+1  else 0

    print (p[0], p[1])
solution()