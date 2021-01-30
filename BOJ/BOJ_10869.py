#BOJ_10869
num = input().split()
oper = ['+', '-', '*', '//', '%']
for i in oper:
    print(eval(i.join(num)))

