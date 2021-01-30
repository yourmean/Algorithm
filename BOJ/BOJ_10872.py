#BOJ_10872

def factorial(n):
    if n==1 or n==0:
        ans= 1
    else:
        ans= n*factorial(n-1)
    return ans
print(factorial(int(input())))