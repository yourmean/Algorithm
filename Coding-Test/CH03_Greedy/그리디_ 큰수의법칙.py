'''
큰 수의 법칙: 다양한 수로 이루어진 배열이 있을 때, 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없음
배열의 크기 N, 숫자가 더해지는 횟수  M, K 가 주어질 때, 큰 수의 법칙에 따른 결과?
'''

def solution():
    N,M,K= map(int, input().split())
    num= list(map(int, input().split()))
    num.sort()
    answer=0

    for i in range(1,M+1):
        if i//K != 0 and i%K == 1:
            answer+=num[-2]
        else:
            answer+=num[-1]
        print(answer)
    return answer
solution()


# Sol1 - fail
# 2번째 max값은 한번만 있으면 됨
N, M, K = map(int, input().split(' '))
num= sorted(input().split())
ans, cnt = 0, 0

for i in range(M):
    if (cnt//K)%2==0:
        ans+=num[0]
    else:
        ans+=num[1]
    cnt+=1
print(ans)