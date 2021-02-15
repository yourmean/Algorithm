'''
거스름돈으로 사용할 500, 100, 50, 10원짜리 동전이 무한히 존재할 때,
거슬러 줘야 할 돈이 N원일 때의 거슬러 줄 동전의 최소 개수?
'''

N=int(input())
coins= [500, 100, 50, 10]
ans= 0
    
for c in coins:
    answer+= N//c
    N-= (N//c)*c    # N%=c (O)

print(ans)