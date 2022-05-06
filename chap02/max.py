from typing import Any, Sequence

def max_of(a : Sequence) -> Any:
    maximum = a[0]
    for i in range(1, len(a)):
        if maximum < a[i]:
            maximum = a[i]

    return maximum

if __name__ == "__main__" :
    num = int(input('배열의 원소 수: '))
    ss = [None] * num

    for i in range(0, num):
        ss[i] = int(input('배열의 %d번째 값: ' % (i + 1)))

    print('최댓값은 %d입니다.' % max_of(ss))
