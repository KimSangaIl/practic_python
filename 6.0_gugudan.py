for n in range(2, 10):
    print(f'#  {n}단   #', end = " ")
print()
for i in range(1, 10):
    for j in range(2, 10):
        print(f'{j} x {i} = {(j * i):2.0f}', end = " ")
    print()