#BOJ_2869
import sys
import math

a,b,v=map(int, sys.stdin.readline().split(' '))
print(math.ceil((v-b)/(a-b)))

# ceil) 4.2일 > 5일로 올림