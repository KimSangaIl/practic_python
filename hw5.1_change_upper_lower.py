## 학번: 2019038041 이름: 김상일 ##
## 전역 변수 선언 ##
inss, outss = "", ""

## 메인 코드 ##
if __name__ == "__main__" :
    inss = input("문자열을 입력하세요 : ")

    for i in range(0, len(inss)) :
        if (inss[i].isupper() == True) :
            outss += inss[i].lower()
        else :
            outss += inss[i].upper()

    print("대소문자 변환 결과 --> %s" % outss)
