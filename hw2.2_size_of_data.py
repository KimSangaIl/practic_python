## 2019038041 김상일 ##

import sys

## 메인 함수 부분 ##
if __name__ == "__main__" :
    intVar = 0
    floatVar = 0.0
    boolVar = True
    strVar = ' '
    listVar = []
    tupleVar =()
    dictVar = {}
    setVar = set()

    print(type(intVar), '기본 크기 -->', sys.getsizeof(intVar))
    print(type(floatVar), '기본 크기 -->', sys.getsizeof(floatVar))
    print(type(boolVar), '기본 크기 -->', sys.getsizeof(boolVar))
    print(type(strVar), '기본 크기 -->', sys.getsizeof(strVar))
    print(type(listVar), '기본 크기 -->', sys.getsizeof(listVar))
    print(type(tupleVar), '기본 크기 -->', sys.getsizeof(tupleVar))
    print(type(dictVar), '기본 크기 -->', sys.getsizeof(dictVar))
    print(type(setVar), '기본 크기 -->', sys.getsizeof(setVar))
