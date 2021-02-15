'''
N*M 형태의 숫자 카드 배열, 선택된 행에 포함된 카드들 중 숫자가 가장 작은 카드 pick
최종적으로 가장 높은 숫자의 카드를 뽑는 전략?
'''

def solution():
    n,m= map(int, input().split())

    card=[]
    for i in range(n):
        num= list(map(int, input().split()))
        card.append(min(num))
    return max(card)
solution()

# 각 행마다 가장 작은 수 찾고 > 그 중 가장 큰 수 pick