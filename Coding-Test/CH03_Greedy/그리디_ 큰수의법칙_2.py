'''
큰 수의 법칙: 다양한 수로 이루어진 배열이 있을 때, 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없음
배열의 크기 N, 숫자가 더해지는 횟수  M, K 가 주어질 때, 큰 수의 법칙에 따른 결과?
'''

def solution():
    N, M, K = map(int, input().split())
    num= list(map(int, input().split()))
    num.sort()

    answer= (num[-1]*K + num[-2]) * M//(K+1)
    answer+= num[-1] * (M%(K+1))

    return answer
solution()

'''
n,m,k= 5, 7, 3, 배열 [2,4,5,4,6]일 때 -> 6 6 6 5 / 6 6 6 의 순서로 더해 나감
1st answer= 반복되는 수열의 길이 K+1의 수 count: M//(K+1)
2nd answer= 1st에 남아있는 수열만큼 num[-1]값 +: M%(K+1)
'''