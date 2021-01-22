#BOJ_2562

n=[]
for i in range(9):
    n.append(int(input()))
m=max(n)
print(m, n.index(m)+1, sep='\n')