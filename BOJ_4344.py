#BOJ_4344

for i in range(int(input())):
    num =list(map(int, input().split(' ')))
    n=num[0]
    del num[0]
    ave=sum(num)/n
    print("{:.3f}%".format(len([x for x in num if x>ave])/n*100))

# format:  {폭.정밀도f}% ~~~ 그만 까먹자!
