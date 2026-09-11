digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
f = open('input.txt')
intro = []
minus = 0
for line in f:
    intro.append(line.split())
system = ''.join(intro[2])
system = int(system)
numbers = [int(x, system) for x in intro[0]]
operation = ''.join(intro[1])
result_1 = numbers[0]
for n in range(1, len(numbers)):
    if operation == '+':
        result_1 += numbers[n]
    elif operation == '-':
        result_1 -= numbers[n]
    elif operation == '*':
        result_1 *= numbers[n]
f.close()
result_end = ''
if result_1 == 0:
    print(result_1)
elif result_1 < 0:
    result_1 = abs(result_1)
    minus += 1
else:
    pass
res_temp = result_1
if system == 2:
    result_end = (bin(result_1)[2:])
elif system == 8:
    result_end = (oct(result_1)[2:])
elif system == 16:
    result_end = (hex(result_1)[2:])
elif system == 1:
    print('Нет результата')
else:
    while res_temp > 0:
        result_end = digits[res_temp % system] + result_end
        res_temp //= system
if minus == 1:
    result_end = '-'+ result_end
f.close()
f = open('output.txt', 'w')
f.write(result_end)
<<<<<<< HEAD
f.close()
=======
f.close()
>>>>>>> 4c93fded177eb75e605702d8295e0d86c7a26135
