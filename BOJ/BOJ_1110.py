#BOJ_1110

n=int(input())
check=n
cnt, temp, new = 0,0,0

while True:
    temp = n//10 + n%10 #자릿수합
    new = (n%10)*10 + temp%10 #새로운 수 = (원래수의 일의자리수)*10 + 합의 일의자리수
    n=new #update n
    cnt+=1
    if n==check:
        print(cnt) #사이클 길이
        break