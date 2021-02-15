'''
N이 1이 될 때까지 다음 두 과정 중 하나 반복적으로 수행
1) N-1  2) N/K
N이 1이 되기까지 수행해야 하는 최소 횟수?
'''

def solution():
    n,k = map(int, input().split())
    cnt= 0

    while True:
        if n==1:
            break
        elif n%k==0:
            n/=k
            cnt+=1
        else:
            n-=1
            cnt+=1
    return cnt
solution()