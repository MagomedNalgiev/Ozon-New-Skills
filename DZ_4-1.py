shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
         'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
         'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}

# Выводим жанр фильма Ведьмак
print(f'Жанр фильма Ведьмак: {shows["Ведьмак"]}')
print('--------------\n')

# Выводим список всех фильмов в словаре
print(f'Список фильмов в словаре:')
for key in shows.keys():
  print(key)
print('--------------')

# Выводим список всех жанров в словаре
print(f'\nСписок жанров в словаре:')
for value in shows.values():
  print(value)
print('--------------')