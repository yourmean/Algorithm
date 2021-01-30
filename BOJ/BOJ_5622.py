#BOJ_5622

n=input().lower()
dial=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

ans=0
for i in range(len(n)):
    for d in dial:
        if n[i] in d:
            ans+= 3+dial.index(d)
print(ans)