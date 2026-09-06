f = open('input.txt')
intro = []
for line in f:
    intro.append(line.split())
numbers = list(map(int, intro[0]))
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
f = open('output.txt', 'w')
result_1 = str(result_1)
f.write(result_1)