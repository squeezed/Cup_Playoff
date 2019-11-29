# Скрипт формирования пар для 1/8 финала в соответствии со следующими условиями:
# 1. Игроки, занявшие 1-е места в своей группе, между собой не играют;
# 2. Игроки, занявшие 2-е места в своей группе, между собой не играют;
# 3. Игроки, вышедшие в плэй-офф из одной группы, между собой не играют.
# Результат жеребьевки выводится на экран и в выходной файл ./result/main_playoff.txt

from random import choice, shuffle

with open('./config/main_playoff.txt', 'r', encoding='utf8') as conf:
    raw = conf.read().splitlines()
result = []

# Распределяем игроков по 2 корзинам в зависимости от занятого места
first_bucket, second_bucket = [], []
for line in raw:
    if line and not line.startswith('#'):
        if tuple(line.split('|'))[2] == '1':
            first_bucket.append(tuple(line.split('|')))
        else:
            second_bucket.append(tuple(line.split('|')))

# Перемешиваем корзины для интриги:)
shuffle(first_bucket)
shuffle(second_bucket)

# Составляем пары с учетом того, чтобы не было двух игроков из одной группы
for player in first_bucket:
    enemy = choice(second_bucket)
    while player[1] == enemy[1]:
        enemy = choice(second_bucket)
    result.append((player, enemy))
    second_bucket.remove(enemy)

# Выводим пары на экран и пишем в файл
with open('./result/main_playoff.txt', 'w', encoding='utf8') as output:
    for idx, pair in enumerate(result):
        output.write('Стол {}:\n{} - {}\n'.format(idx + 1, pair[0][0], pair[1][0]))
        print('Стол {}:\n{} - {}'.format(idx + 1, pair[0][0], pair[1][0]))

input('Нажмите Enter для выхода...')
