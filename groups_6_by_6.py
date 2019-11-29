# Скрипт формирования 6 групп по 6 человек для группового этапа
# Группы формируются из нескольких корзин, распределение по корзинам выполняется по рейтингу
# Результат выводится на экран, а также в файл ./result/groups_6_by_6.txt

from random import shuffle

LETTERS = 'ABCDEF'


def get_name(record):
    # Функция получения имени игрока из строки вида Nickname|Rating
    return str(record.split('|')[0])


def get_rating(record):
    # Функция получения рейтинга игрока из строки вида Nickname|Rating
    return int(record.split('|')[1])


with open('./config/groups_6_by_6.txt', 'r', encoding='utf8') as raw:
    raw_players = [x for x in raw.read().splitlines() if x and not x.startswith('#')]
result = []

# Сортируем игроков по рейтингу, далее распределяем по корзинам (в данном случае - 6 корзин по 6 игроков)
players = sorted(raw_players, key=get_rating, reverse=True)
players_by_buckets = [players[:6], players[6:12], players[12:18], players[18:24], players[24:30], players[30:]]

# Перемешиваем каждую из корзин для интриги:)
for lst in players_by_buckets:
    shuffle(lst)

# Записываем распределение по группам в файл и выводим на экран
with open('./result/groups_6_by_6.txt', 'w', encoding='utf8') as out:
    for idx in range(6):
        out.write('Группа {}:\n'.format(LETTERS[idx]))
        print('Группа {}:\n'.format(LETTERS[idx]))
        for num_b, bucket in enumerate(players_by_buckets, start=1):
            out.write('{}. {} - {}\n'.format(num_b, get_name(bucket[idx]), get_rating(bucket[idx])))
            print('{}. {} - {}\n'.format(num_b, get_name(bucket[idx]), get_rating(bucket[idx])))
        out.write('\n')
        print('\n')
