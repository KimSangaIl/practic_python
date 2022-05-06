print('1부터 n까지 합을 구합니다.')
n = int(input('n값을 입력하세요 : '))

i = 1
hap = 0

while i <= n :
    hap += i
    i += 1

print('1부터 %d까지 정수의 합은 %d입니다.' % (n, hap))
