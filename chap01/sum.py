print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('a값을 입력하세요 : '))
b = int(input('b값을 입력하세요 : '))

if a > b: a, b = b, a
hap = 0
for i in range(a, b + 1): hap += i

print('a부터 b까지 정수의 합은 %d입니다.' % hap)
