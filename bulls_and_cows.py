from random import randint


difficult = 4
num = [i for i in range(1, 10)]
gamenumber_list = [str(num.pop(randint(0, len(num) - 1))) for i in range(difficult)]
gamenumber = ''.join(gamenumber_list)


def main():
    while True:
        move(gamenumber)
        print(f'{playernumber}: {compare(gamenumber, playernumber)[0]} быка, {compare(gamenumber, playernumber)[1]} коров')
        if compare(gamenumber, playernumber)[0] == 4:
            print('Мууу! Победа!')
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


print('Добро пожаловать!\nКомпьютер уже загадал число. Давайте же начнем!')
main()