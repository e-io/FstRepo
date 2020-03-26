# Программа считывает зашифрованную строку из бинарного файла
# Далее из другого файла считывает пароли
# Программа применяет каждый пароль чтобы расшифровать строку

import simplecrypt as sc

with open('encrypted.bin', 'rb') as ecb:
    string = ecb.read()

print(f'String is {string}\n')

with open('passwords.txt') as pwtxt:
    pws = pwtxt.read().strip().split()

for pw in pws:
    try:
        print(f'We try password {pw}')
        print(sc.decrypt(pw, string))
        print(f'This password is good\n')
    except:
        print(f'This password is bad\n')