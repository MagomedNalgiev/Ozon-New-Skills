import random

shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
         'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
         'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,
           'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}

# Копируем словарь для дальнейшего удаления значений, чтобы исключить дубли рекомендаций
shows_copy = shows.copy()
print(f'Советуем вам посмотреть:')

while True:
  try:
    # Присваиваем случайный фильм переменной random_movie
    random_movie = random.choice(list(shows_copy.keys()))
    # Условие, чтобы программа работала только с фильмами рейтингом выше 0.85 и не предлагала фильмы с жанром "фэнтази"
    if shows_copy.pop(random_movie) != 'фэнтази' and ratings.get(random_movie) >= 0.85:
        print(f'\n{random_movie}\n')

        answer = input('Вам подходит этот сериал? \n(Напишите Да или Нет)\n').lower()

        # Задаем условие, чтобы программа принимала только ответы "да" или "нет"
        while answer != 'нет' and answer != 'да':
          answer = input(f'Пожалуйста, введите Да или Нет\n').lower()

          if answer != 'да' and answer != 'нет':
            continue
          else:
            break

        # Задаем условие, чтобы программа остановилась, если ответ "да" и продолжила работу, если ответ "нет"
        if answer == 'да':
          break
        elif answer == 'нет':
          continue

    # Условие, чтобы программа подобрала новый фильм, если выбранное значение не соответствует условиям поиска
    else:
      continue

  # Задаем исключение, чтобы программа остановилась, когда в словаре закончатся фильмы соответстующие условиям поиска
  except IndexError:
    print('Вы дошли до конца списка')
    break