import random

a1 = random.randrange(1, 6)
a2 = random.randrange(1, 6)
b1 = random.randrange(1, 6)
b2 = random.randrange(1, 6)
ra = a1 + a2
rb = b1 + b2

print(f'A\'s dice number is {a1}, {a2}')
print(f'B\'s dice number is {b1}, {b2}')
if ra > rb: print('A win')
elif ra < rb: print('B win')
else: print('draw')