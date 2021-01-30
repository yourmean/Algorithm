#BOJ_10952

while True:
    s=sum(map(int, input().split()))
    if s == 0:  # 0<A,B<10
        break
    print(s)