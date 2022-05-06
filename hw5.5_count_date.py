## 학번: 2019038041 이름: 김상일 ##
from time import *
from datetime import *

## 함수 선언 ##
def countdays(d1, d2) :
    count = 0
    year, month, day = d1.split('/')
    startday = date(int(year), int(month), int(day))
    year, month, day = d2.split('/')
    pastday = date(int(year), int(month), int(day))
    diff = pastday - startday
    count = diff.days
    return count

def tday(d) :
    weeks = ['월', '화', '수', '목', '금', '토', '일']
    return weeks[d.tm_wday]

## 전역 변수 선언 ##
startdate, pastdate, nowtime = ' ', ' ', None

## 메인 코드 ##
if __name__ == "__main__" :
    startdate = input('시작 날짜(연/월/일) --> ')
    nowtime = localtime()
    pastdate = str(nowtime.tm_year) + '/' + str(nowtime.tm_mon) + '/' + str(nowtime.tm_mday)
    print(startdate, '부터 오늘(' , pastdate, ')까지는 ', countdays(startdate, pastdate), '일이 지났습니다')
    print('그리고 오늘은 ', tday(nowtime), '요일입니다')
