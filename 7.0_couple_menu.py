menu = {'떡볶이':'오뎅', '짜장면':'단무지', '라면':'김치', '피자':'피클', '맥주':'땅콩', '치킨':'치킨무', '삼겹살':'상추'};
while(True):
    food = input(f'{list(menu.keys())} 중 좋아하는 음식은? ')
    if food in menu:
        print(f'{food} 궁합 음식은 {menu.get(food)}입니다')
    elif food == '끝':
        print('종료합니다.')
        break
    else:
        print('음식을 잘못 입력하셨습니다.')