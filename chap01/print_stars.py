print('*을 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))
p = int(input('몇 개마다 줄바꿈할까요?: '))

for i in range(0, n // p):
    for j in range(0, p): print('*', end = '')
    print()

for k in range(0, n % p): print('*', end = '')
