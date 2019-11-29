# Скрипт формирования 8 групп по 4 человека для группового этапа
# Группы формируются из нескольких корзин, распределение по корзинам выполняется по рейтингу
# Результат выводится на экран, а также в файл ./result/groups_8_by_4.txt

from random import shuffle

LETTERS = 'ABCDEFGH'


def get_name(record):
    # Функция получения имени игрока из строки вида Nickname|Rating
    return str(record.split('|')[0])


def get_rating(record):
    # Функция получения рейтинга игрока из строки вида Nickname|Rating
    return int(record.split('|')[1])


with open('./config/groups_8_by_4.txt', 'r', encoding='utf8') as raw:
    raw_players = [x for x in raw.read().splitlines() if x and not x.startswith('#')]
result = []

# Сортируем игроков по рейтингу, далее распределяем по корзинам (в данном случае - 4 корзины по 8 игроков)
players = sorted(raw_players, key=get_rating, reverse=True)
players_by_buckets = [players[:8], players[8:16], players[16:24], players[24:]]
for lst in players_by_buckets:
    shuffle(lst)

# Записываем распределение по группам в файл и выводим на экран
with open('./result/groups_6_by_4.txt', 'w', encoding='utf8') as out:
    for idx in range(4):
        out.write('Группа {}:\n'.format(LETTERS[idx]))
        print('Группа {}:\n'.format(LETTERS[idx]))
        for bucket in players_by_buckets:
            out.write('{}. {} - {}\n'.format(idx + 1, get_name(bucket[idx]), get_rating(bucket[idx])))
            print('{}. {} - {}\n'.format(idx + 1, get_name(bucket[idx]), get_rating(bucket[idx])))
        out.write('\n')
        print('\n')
