import time

max = 86399

a, b, c = 0, 0, 0

while True:
  if a == 60:
    a, b = a % 60, b + 1
    if b == 60:
      b, c = b % 60, c + 1
  print(f'{c} часов, {b} минут, {a} секунд')
  time.sleep(1)
  a += 1
  if a > max:
    print('1 день, 0 часов, 0 минут, 0 секунд')
    break
