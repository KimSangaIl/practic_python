n1, n2, add, res = [0] * 4

n1 = int(input('input first number: '))
n2 = int(input('input second number: '))
add = int(input('input adding number: '))
for i in range(n1, n2 + 1, add):
    res += i
print(f'{n1} + {n1 + add} + ... + {n2} = {res}')