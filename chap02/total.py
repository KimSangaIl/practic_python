score1 = int(input('1번 학생의 점수를 입력하세요: '))
score2 = int(input('2번 학생의 점수를 입력하세요: '))
score3 = int(input('3번 학생의 점수를 입력하세요: '))
score4 = int(input('4번 학생의 점수를 입력하세요: '))
score5 = int(input('5번 학생의 점수를 입력하세요: '))

hap = 0
ave = 0
hap += score1
hap += score2
hap += score3
hap += score4
hap += score5
ave = hap / 5

print('합계는 %d점 입니다.' % hap)
print('평균은 %d점 입니다.' % ave)
