# Программа считывает файл из input.txt
# и вставляет текст в обратном порядке в output.txt
a = []
with open('input.txt', 'rt') as file:
    for line in file:
        a.append(line.rstrip())
with open('output.txt', 'wt') as file:
    file.write('\n'.join(reversed(a)))

