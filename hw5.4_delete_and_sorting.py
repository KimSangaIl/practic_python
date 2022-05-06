## 학번: 2019038041 이름: 김상일 ##
import random

## 함수 선언 ##
def delch(ssdata) :
    numdata = ' '
    for ch in ssdata :
        if ch.isdigit():
            numdata += ch

    return int(numdata)

## 전역 변수 선언 ##
data = []

## 메인 코드 ##
if __name__ == "__main__" :
    for i in range(0, 10) :
        temp = hex(random.randrange(0, 10000))
        temp = temp[2:]
        data.append(temp)

    print('정렬 전 데이터 : ', end = ' ')
    [print(num, end = ' ') for num in data]

    for i in range(0, len(data) - 1 ) :
        for j in range(i + 1, len(data)) :
            if delch(data[i]) > delch(data[j]) :
                temp = data[i]
                data [i] = data[j]
                data[j] = temp

    print('\n정렬 후 데이터 : ', end = ' ')
    [print(num, end = ' ') for num in data]
                   
