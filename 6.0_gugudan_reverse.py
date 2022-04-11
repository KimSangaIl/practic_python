for n in range(9, 1, -1):
    print(f'#  {n}단   #', end = " ")
print()
for i in range(9, 0, -1):
    for j in range(9, 1, -1):
        print(f'{j} x {i} = {(j * i):2.0f}', end = " ")
    print()