#BOJ_10871

a,b=map(int, input().split())
num=list(map(int, input().split()))
for i in num:
    if i<b:
        print(i)