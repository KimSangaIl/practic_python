for i in range(8, -1, -2):
    for k in range(i): print(' ', end = '')
    for j in range(1, (10 - i)): print('\u2605', end = ' ')
    print()

for a in range(2, 9, 2):
    for c in range(a): print(' ', end = '')
    for b in range((10 - a - 1), 0, -1): print('\u2605', end = ' ')
    print()