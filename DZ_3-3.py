import random

speech_1 = ['Коллеги,', 'В то же время,', 'Однако,', 'Тем не менее,', 'Следовательно,', 'Соответственно,',
            'Вместе с тем,', 'С другой стороны,']
speech_2 = ['парадигма цифровой экономики', 'контекст геймификации', 'дижитализация бизнес-процессов',
            'прагматичный подход к облачным платформам', 'совокупность сквозных технологий',
            'программа прорывных исследований', 'ускорение блокчейн-транзакций', 'экспоненциальный рост Big Data']
speech_3 = ['открывает новые возможности для', 'выдвигает новые требования', 'несет в себе риски',
            'расширяет горизонты', 'заставляет искать варианты', 'не оставляет шанса для', 'повышает вероятность',
            'обостряет проблему']
speech_4 = ['дальнейшего углубления', 'бюджетного финансирования', 'синергетического эффекта',
            'компроментации конфиденциальных', 'несанкционированной кастомизации' 'нормативного регулирования',
            'практического применения']
speech_5 = ['знаний и компетенций.', 'непроверенных гипотез.', 'волатильных активов.', 'опасных экспериментов.',
            'государственно-частных партнеров.', 'цифровых следов граждан.', 'нежелательных последствий.',
            'случайных открытий.']


#Создаем пустой массив для хранения фраз
speech_massive = []


#Создаем перменную, в которой будет храниться рандомное число от 5 до 10
count = random.randint(5, 10)


#Запускаем цикл по генерации фраз до заданного количества
while len(speech_massive) < count:
    speech = [random.choice(speech_1)] + [random.choice(speech_2)] + [random.choice(speech_3)] + [
        random.choice(speech_4)] + [random.choice(speech_5)]
    speech_massive.append(speech)


#Выводим каждую фразу на отдельной строке
for i in speech_massive:
    print(*i)