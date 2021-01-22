#BOJ_8958

def score():
    n=list(str(input()))
    cnt=0
    score=0
    for i in range(len(n)):
        if n[i]=='O':
            cnt+=1
            score+=cnt
        else:
            cnt=0
    print(score)

N=int(input())
for i in range(N):
    score()