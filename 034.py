s_list = [3, 1, 1, 2, 0, 0, 2, 3, 3]

max_val = s_list[0]
min_val = s_list[0]

for elem in s_list: #for loop가 돌아가면서 순서대로 원소들의 크기를 비교함
    if elem > max_val:
        max_val = elem
    if elem < min_val:
        min_val = elem

print(f"max: {max_val}")
print(f"min: {min_val}")
