#BOJ_1152

s=input()
if s == ' ':
    print(0)
else:
    print(s.strip(' ').count(' ')+1)
    
#1) input이 공백일 때 ouput 1
#2) input이 ' a'일 때 ouput 0
#만만하게 봤다가 얻어맞은 문제ㅎ