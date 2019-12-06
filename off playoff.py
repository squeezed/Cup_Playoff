#! /usr/bin/python3
# Скрипт случайного формирования пар плей-офф, без учета занятых мест и групп
# Используется в жеребьевке утешительного плей-офф и плей-офф по системе Double Elimination

from random import sample

if __name__ == '__main__':
    with open('./config/off_playoff.txt', 'r', encoding='utf8') as conf:
        players = [x for x in conf.read().splitlines() if x and not x.startswith('#')]
    # Цикл формирования случайных пар
    result = []
    while len(players) != 0:
        pair = sample(players, k=2)
        result.append(pair)
        for player in pair:
            players.remove(player)

    # Вывод результатов жеребьевки
    with open('./result/off_playoff.txt', 'w', encoding='utf8') as out:
        for idx, table in enumerate(result, start=1):
            out_line = 'Стол {}:\n{} - {}\n'.format(idx, table[0].split('|')[0], table[1].split('|')[0])
            print(out_line)
            out.write(out_line)

input('Нажмите Enter для выхода...')
