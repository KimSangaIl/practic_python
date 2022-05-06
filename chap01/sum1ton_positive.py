print('1부터 n까지 정수의 합을 구합니다.')

while True:
    n = int(input('n의 값을 입력하세요: '))
    if n > 0: break;

hap = 0
for i in range(1, n + 1):
    hap += i

print('1부터 %d까지 정수의 합은 %d입니다.' % (n, hap))
