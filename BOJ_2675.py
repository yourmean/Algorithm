#BOJ_2675

for _ in range(int(input())):
    cnt, text = input().split()
    for i in text:
        print(i*int(cnt), end='')
    print()
    
#마지막에 print() 까먹고 i, text, cnt 자꾸 혼용해서 썼다 ㅠㅠ