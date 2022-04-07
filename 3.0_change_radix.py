radix = int(input("input radix number(16/10/8/2) : "))
num = input("input number : ")

if radix == 16 :
    num10 = int(num, 16)
elif radix == 10 :
    num10 = int(num, 10)
elif radix == 8 :
    num10 = int(num, 8)
elif radix == 2 :
    num10 = int(num, 2)
else :
    print("Enter only one of the numbers 16, 10, 8, and 2.\n")
    exit()

print("hexadecimal ==> ", hex(num10))
print("decimal number ==> ", num10)
print("octal number ==> ", oct(num10))
print("binary number ==> ", bin(num10))
