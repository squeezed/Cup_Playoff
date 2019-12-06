#! /usr/bin/python3
# Формирование пар плей-офф из двух и более корзин
# Между собой не играют:
# 1. Игроки, занявшие одно и то же место в группе
# 2. Игроки, вышедшие в плей-офф из одной группы

from random import sample
from itertools import chain


def check_place(line1, line2):
    # Функция проверки занятых мест в группе
    # Если места одинаковые, то не подходит, возвращаем False, иначе - True
    if line1.split('|')[2] != line2.split('|')[2]:
        return True
    else:
        return False


def check_group(line1, line2):
    # Функция проверки группы выхода в плей-офф
    # Если группа одинаковая, то не подходит, возвращаем False, иначе - True
    if line1.split('|')[1] != line2.split('|')[1]:
        return True
    else:
        return False


if __name__ == '__main__':
    with open('./config/main_playoff.txt', 'r', encoding='utf8') as conf:
        players = [x for x in conf.read().splitlines() if x and not x.startswith('#')]
    # Цикл формирования пар по заданным условиям
    # Если последняя пара не попадает под необходимые условия - запускаем цикл жеребьевки повторно
    # Если попадает - цикл завершится штатно по условию выхода
    result = []
    while len(players) != 0:
        pair = sample(players, k=2)
        if len(players) > 2:
            if check_group(pair[0], pair[1]) and check_place(pair[0], pair[1]):
                result.append(pair)
                for player in pair:
                    players.remove(player)
        else:
            if check_group(pair[0], pair[1]) and check_place(pair[0], pair[1]):
                result.append(pair)
                for player in pair:
                    players.remove(player)
            else:
                result.append(pair)
                players = list(chain.from_iterable(result))
                result = []

    # Выводим результаты жеребьевки
    with open('./result/main_playoff.txt', 'w', encoding='utf8') as out:
        for idx, table in enumerate(result, start=1):
            out_line = 'Стол {}:\n{} - {}\n'.format(idx, table[0].split('|')[0], table[1].split('|')[0])
            print(out_line)
            out.write(out_line)

print('Нажмите Enter для выхода...')
