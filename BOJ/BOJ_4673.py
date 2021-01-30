#BOJ_4673

def ans():
    self_num = []
    for i in range(1, 10001):
        s = list(str(i))
        temp = i + sum([int(x) for x in s])
        if temp <= 10000:
            self_num.append(temp)

    self_num = sorted(set(self_num))

    for i in range(1, 10001):
        if i in self_num:
            continue
        else:
            print(i)

ans()