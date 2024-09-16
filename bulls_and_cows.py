#Крутость хода coolnes_of_move

#импортирование библиотек
from random import randint


#главный цикл
def main():
    start()
    difficult()
    while True:
        move(gamenumber)
        if not current(compare(gamenumber, playernumber)[0], compare(gamenumber, playernumber)[1]):
            break
            

#выполнение хода (обработка введенного игроком числа)
def move(gamenumber):
    global playernumber
    while True:
        try:
            playernumber = int(input(('Сделать ход: ')))
            if len(str(playernumber)) != len(str(gamenumber)):
                print(f'Необходимо ввести число стостоящее из {len(str(gamenumber))} цифр. Попробуйте ещё раз.')
            elif similar(playernumber):
                print('Цифры не могут повторяться. Попробуйте ещё раз.')
            else:
                break
        except ValueError:
            print('Недопустимый ввод. Попробуйте ещё раз: ')


#подсчет быков и коров (сравнение числа игрока и загаданного компьютером)
def compare(gamenumber, playernumber):
    bulls = 0
    cows = 0
    gamenumber = str(gamenumber)
    playernumber = str(playernumber)
    for i in range(len(gamenumber)):
        if gamenumber[i] == playernumber[i]:
            bulls += 1
        elif gamenumber[i] in playernumber:
            cows += 1
    return (bulls, cows)


#обработка и вывод результатов хода
def current(bulls, cows):
    if bulls == len(str(gamenumber)):
        print('Мууу! Победа!')
        return False
    if bulls in [0, 5, 6, 7, 8, 9, 10]:
        message_bulls = 'быков'
    elif bulls == 1:
        message_bulls = 'бык'
    else:
        message_bulls = 'быка'
    if cows in [0, 5, 6, 7, 8, 9, 10]:
        message_cows = 'коров'
    elif cows == 1:
        message_cows = 'корова'
    else:
        message_cows = 'коровы'
    print(f'{playernumber}: {bulls} {message_bulls}, {cows} {message_cows}')
    return True


#установка сложности игры
def difficult():
    global gamenumber
    while True:
        try:
            diff = int(input('Установите сложность игры: '))
            num = [i for i in range(0, 10)]
            gamenumber_list = [str(num.pop(randint(0, len(num) - 1))) for i in range(diff)]
            gamenumber = ''.join(gamenumber_list)
            break
        except ValueError:
            print('Недопустимый ввод. Попробуйте ещё.')


#проверка на совпадение цифр в числе
def similar(number):
    for i in range(1, len(str(number))):
        if str(number)[i - 1] == str(number)[i]:
            return True
    return False


#приветственные слова
def start():
    print('Добро пожаловать!\nКомпьютер уже загадал число. Давайте же начнем!')


main()