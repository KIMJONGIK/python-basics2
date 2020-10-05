apart = [[101, 102, 103, 104], [201, 202, 203, 204], [301, 302, 303, 304], [401, 402, 403, 404]]
arrears = [101, 203, 301, 404]

for i in range(0, 4):
    for j in range(0, 4):
        if apart[i][j] in arrears:
            pass
        else:
            print(f'Newpaper delivery: {apart[i][j]}')


