#BOJ_10250

for i in range(int(input())):
    h, w, n = map(int, input().split(' '))
    if n%h!=0:
        print(str(n%h)+str(n//h+1).zfill(2))
    else:
        print(str(h)+str(n//h).zfill(2)) #배수관계 예외처리