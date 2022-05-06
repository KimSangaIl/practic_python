## 2019038041 김상일 ##

##변수 선언 부분##
strVar = ''

##메인 코드 부분##
if __name__ == "__main__" :
    strVar = input('문자열을 입력 --> ')

    for i in range(len(strVar) -1, -1, -1) :
        print('%c' %strVar[i], end = '')
