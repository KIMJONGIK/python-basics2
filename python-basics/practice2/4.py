for i in range(1, 100):
    count = 0
    j = str(i)
    if j.find('3') >= 0:
        j = j.replace('3', '0', 1)
        count += 1
    else:
        count == count

    if j.find('6') >= 0:
        j = j.replace('6', '0', 1)
        count += 1
    else:
        count = count

    if j.find('9') >= 0:
        j = j.replace('9', '0', 1)
        count += 1
    else:
        count = count

    if count > 0:
        print('{0} {1}'.format(i, '짝' * count))


