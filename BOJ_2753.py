#BOJ_2753
#https://www.acmicpc.net/problem/2753

n=int(input())

# 4의배수& not 100의 배수이거나 400의 배수이면 -> 윤년 -> 1
# int 까먹었더니 True로 출력돼서 틀렸음,,
print(int((n%4==0 and n%100!=0)or(n%400==0)))

