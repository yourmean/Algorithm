#BOJ_15552

import sys
n=int(input())
for i in range(n):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)

# 코랩에서는 ValueError가 나는데 백준에서는 잘 돌아간다