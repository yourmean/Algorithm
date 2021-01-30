#BOJ_10809

s = input()
alp = list(range(97,123))

for a in alp:
    print(s.find(chr(a)))

# range(97,123) : 알파벳 소문자 아스키코드 범위