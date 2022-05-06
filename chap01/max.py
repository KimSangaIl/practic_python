a = int(input('정수 a의 값을 입력하세요 : '))
b = int(input('정수 b의 값을 입력하세요 : '))
c = int(input('정수 c의 값을 입력하세요 : '))

maximum = a

if maximum < b: maximum = b
if maximum < c: maximum = c

print('최댓값은 %d입니다.' % maximum)
