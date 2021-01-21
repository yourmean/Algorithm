#BOJ_2884
#https://www.acmicpc.net/problem/2884

# sol2)
h,m = map(int, input().split(' '))

# m<45면 h-1, m>=45면 h 그대로 -> 시
# (m-45)%60 -> 분
print((h-(m<45))%24, (m-45)%60)