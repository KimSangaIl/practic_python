for i in range(3, 101):
    for j in range(2, i):
        if i % j == 0: break
    if (j == i - 1): print(f'{i}', end = ' ')