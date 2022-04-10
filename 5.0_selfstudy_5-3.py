n = int(input('input number : '))
for i in range(2, n):
    if n % i == 0:
        print(f'{n} is not sosu')
        break
    else: pass
if i == n - 1: print(f'{n} is sosu')
