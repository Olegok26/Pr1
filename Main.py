x = float(input('Первое значение: '))
y = float(input('Второрое значение: '))
operation = input('Operation: ')
result = None
if operation == '+':
 result = x + y
elif operation == '-':
 result = x - y
elif operation == '*':
 result = x * y
elif operation == '/':
 result = x/y
else:
 print('Неподдерживаямая операция')
if result is not None:
 print('Результат:', result)