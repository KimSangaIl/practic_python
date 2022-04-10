select, answer, numStr, n1, n2 = 0, 0, "", 0, 0

select = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계 : "))

if select == 1:
    numStr = input('수식을 입력하세요 : ')
    answer = eval(numStr)
    print(f'{numStr} 결과는 {answer:5.1f} 입니다.')
elif select == 2:
    n1 = int(input('첫번째 숫자를 입력하세요: '))
    n2 = int(input('첫번째 숫자를 입력하세요: '))
    for i in range(n1, n2 + 1):
        answer += i
    print(f'{n1} + ... + {n2} = {answer} 입니다.')
else:
    print('1 또는 2만 입력하세요')