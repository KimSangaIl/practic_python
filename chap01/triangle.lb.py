print('왼쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
n = int(input('짧은 변의 길이를 입력하세요: '))

for i in range(0, n):
    for j in range(0, i + 1):
        print('*', end = '')
    print()

print()

for k in range(0, n):
    for l in range(0, n - k -1):
        print(' ', end = '')
    for m in range(0, k + 1):
        print('*', end = '')
    print()
