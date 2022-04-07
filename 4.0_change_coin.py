## declare variable ##
money, c500, c100, c50, c10 = [0] * 5

## main code ##
money = int(input("How much money to change : "))

c500 = money // 500
print("500coin ==> ", c500)
money %= 500

c100 = money // 100
print("100coin ==> ", c100)
money %= 100

c50 = money // 50
print("50coin ==> ", c50)
money %= 50

c10 = money // 10
print("50coin ==> ", c10)
money %= 10

print("Can't change to coin ==> ", money)
