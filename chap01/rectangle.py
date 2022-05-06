area = int(input('직사각형의 넓이를 입력하세요: '))

for i in range(1, area):
    if i * i > area: break
    if area % i == 0: print(i, 'x', area // i, '\n')
        
