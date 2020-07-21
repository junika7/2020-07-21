l = [3, 1, 1, 2, 0, 0, 2, 3, 3]

d = {}

for n in l:
    if n in d: #n이 d에 있다면
        d[n] += 1 #d에서 n에 대한 value에 1 더하기
    else: #n이 d에 없다면
        d[n] = 1 #value를 1로 설정 > 처음 나오면 1로 설정되고, 또 나오면 if 줄에 의해서 1 추가됨

print(d)

for keys, values in d.items():
    print(keys, ":", values)
