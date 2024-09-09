#Сложность игры
#Крутость хода


from random import randint




def main():
    while True:
        move(gamenumber)
        if not current(compare(gamenumber, playernumber)[0], compare(gamenumber, playernumber)[1]):
            break
            


def move(gamenumber):
    global playernumber
    while True:
        try:
            playernumber = int(input(('Сделать ход: ')))
            if len(str(playernumber)) != len(str(gamenumber)):
                print(f'Необходимо ввести число стостоящее из {len(str(gamenumber))} цифр. Попробуйте ещё раз:')
            else:
                break
        except ValueError:
            print('Недопустимый ввод. Попробуйте ещё раз: ')


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


def current(bulls, cows):
    if bulls == 4:
        print('Мууу! Победа!')
        return False
    if bulls == 0:
        message_bulls = 'быков'
    elif bulls == 1:
        message_bulls = 'бык'
    else:
        message_bulls = 'быка'
    if cows == 0:
        message_cows = 'коров'
    elif cows == 1:
        message_cows = 'корова'
    else:
        message_cows = 'коровы'
    print(f'{playernumber}: {bulls} {message_bulls}, {cows} {message_cows}')
    return True


def difficult():
    global gamenumber
    while True:
        try:
            diff = int(input('Установите сложность игры: '))
            num = [i for i in range(1, 10)]
            gamenumber_list = [str(num.pop(randint(0, len(num) - 1))) for i in range(diff)]
            gamenumber = ''.join(gamenumber_list)
            break
        except ValueError:
            print('Недопустимый ввод. Попробуйте ещё.')


print('Добро пожаловать!\nКомпьютер уже загадал число. Давайте же начнем!')
difficult()
print(gamenumber)
main()