number = int(input('Введите целое число от 3 до 20: '))
keys = ''
for i in range(1, number):
    for j in range(2, number):
        if j <= i:
            continue
        if number % (i + j) == 0:
            keys += str(i) + str(j)
print('Ключ: ', keys)
