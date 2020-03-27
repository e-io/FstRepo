# Данный модуль предоставляет интерфейс к функции primes()
# primes() - это генератор, генерирующий простые числа
# Technology stack: yield

def primes():
    lst = []
    a = 1
    while True:
        a += 1
        is_simple = True
        for n in lst:
            if a % n == 0:
                is_simple = False
                break
        if is_simple:
            lst.append(a)
            yield a

def _test(a):
    from itertools import takewhile

    lst = list(takewhile(lambda x: x <= a, primes()))
    print(f'Simple numbers before {a}:')
    for n in lst:
        print(n)

if __name__ == '__main__':
    _test(2020)