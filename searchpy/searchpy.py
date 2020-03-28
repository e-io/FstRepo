# Данная программа ищет все директории внутри заданной,
# где есть питоновские файлы .py
# результат записывает в файл output.txt
# This program searches for all directories inside the specified folder,
# where there are Python files .py
# writes the result to output.txt
import os

def searchpy(dir):
    with open('output.txt', 'wt') as output:
        for cdir, dirs, files in os.walk(dir):
            for file in files:
                if file[-3:] == '.py':
                    output.write(cdir[2:] + '\n')
                    break

if __name__ == '__main__':
    searchpy('.\main')


