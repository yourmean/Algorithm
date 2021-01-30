#BOJ_2292

n = int(input())
if n == 1:
    dis= 1
else:
    for i in range(1, 20000):
        if 3*i*(i-1)+2 <= n and n <= 3*(i-1)*(i+2)+7:
            dis= i+1
            break
print(dis)