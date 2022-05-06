## 학번 : 2019038041  이름 : 김상일 ##
## 전역 변수 선언 부분 ##
i, k, heartnum = [0] * 3
numStr, ch, heartStr = [None] * 3

## 메인 코드 부분 ##
if __name__ == "__main__" :
    numStr = input("숫자를 여러 개 입력하세요 : ")
    print("")
    i = 0
    ch = numStr[i]
    while True :
        heartnum = int(ch)

        heartStr = ""
        for k in range (0, heartnum) :
            heartStr += "\u2665"
            k += 1

        print(heartStr)

        i += 1
        if (i > len(numStr) - 1) :
            break

        ch = numStr[i]
