#BOJ_3052

a=[]
for i in range(10):
    a.append(int(input())%42)
srr=set(a)
print(len(srr))