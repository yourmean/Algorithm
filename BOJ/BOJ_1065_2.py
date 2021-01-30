#BOJ_1065
print(sum(i<100 or (i//100+i%10)==(i//10%10)*2 for i in range(1,int(input())+1)))

#등차수열 [a b c d], [a b c]
#a+d = b+c, a+c=2b