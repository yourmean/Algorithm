#BOJ_2908

a,b=map(str, input().split(' '))
print(max(int(a[::-1]),int(b[::-1])))