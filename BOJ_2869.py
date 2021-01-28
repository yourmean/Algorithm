#BOJ_2869

a,b,v=map(int, input().split(' '))
cnt= 0
pre= 0
for i in range(1000000000):
    pre+= a
    cnt+=1
    if pre<v:
        pre-= b
    else:
        print(cnt)
        break

#그대로 제출했으면 시간초과 났을 sol1 