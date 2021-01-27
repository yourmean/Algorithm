#BOJ_1712

a,b,c = map(int, input().split(' '))
print(a//(c-b) + 1) if (c-b!=0 and (a//(c-b) + 1)>0) else print(-1)