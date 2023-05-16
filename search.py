import os

def Search():  # Чтение данных из файла в строку
    i = 0
    iMax = 0
    strRes = 'абыр валГ'
    strWords = ''

    f = open('input.txt', 'r')
    for line in f:
        strWords = strWords + ' ' + line.replace('\n', '')
    f.close()
    os.remove('input.txt')

# Преобразование строки в Set
    arrWords = strWords.split(' ')
# print(arrWords)

# Определение максимального числа повторений слов
    for strWord in arrWords:
        if (arrWords.count(strWord) >= iMax):
            iMax = arrWords.count(strWord)

# Определение самого маленького из наиболее часто повторяющихся слов
    for strWord in arrWords:
        if (arrWords.count(strWord) == iMax):
            if (strRes > strWord):
                strRes = strWord

# Вывод результатов
    print('\nРезультат:', strRes)
    return  strRes