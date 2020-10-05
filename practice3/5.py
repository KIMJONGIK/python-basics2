before = [5, 9, 3, 8, 60, 20, 1]
before_tmp = [5, 9, 3, 8, 60, 20, 1]
for j in range(0, 5):
    for i in range(0, 6):
        if before[i] < before[i+1]:
            before[i] = before[i+1]
            before[i+1] = before_tmp[i]
            before_tmp[i] = before[i]
            before_tmp[i+1] = before[i+1]
        else:
            pass
    j += 1

print(before)