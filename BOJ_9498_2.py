#BOJ_9498
#https://www.acmicpc.net/problem/9498

# sol1) 성실하게 if문 써서 풀기
n = int(input())
if 89<n<=100:
    print('A')
elif 79<n<90:
    print('B')
elif 69<n<90:
    print('C')
elif 59<n<90:
    print('D')
else:
    print('F')