print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('a값을 입력하세요 : '))
b = int(input('b값을 입력하세요 : '))

if a > b: a, b = b, a
hap = 0
for i in range(a, b):
    print(i, '+', end = ' ')
    hap += i

hap += b
print(b, '=', hap)
