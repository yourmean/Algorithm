'''
given n, 00:00:00 ~ n:59:59까지 3을 포함하는 시각 count
'''
def solution():
    n= input()
    answer=0

    for i in range(int(n)+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i)+str(j)+str(k):
                    answer+=1
    return answer

solution()