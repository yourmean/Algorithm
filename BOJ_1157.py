#BOJ_1157

s=input().lower()
words=list(set(s))
cnt=[]

for w in words:
    cnt.append(s.count(w))

if cnt.count(max(cnt)) != 1:
    print('?')
else:
    print(words[cnt.index(max(cnt))].upper()) 