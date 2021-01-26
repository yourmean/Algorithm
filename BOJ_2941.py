#BOJ_2941

cr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=' ,'z=']

s=input()
for c in cr:
    s = s.replace(c, '@')

print(len(s))

#print를 까먹지 말자~