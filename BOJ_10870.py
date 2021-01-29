#BOJ_10870

def fibonacci(n):
    if n==0:
        ans=0
    elif n==1:
        ans=1
    else:
        ans= fibonacci(n-2) + fibonacci(n-1)
    return ans

print(fibonacci(int(input())))