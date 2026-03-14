days_of_week = [
    "ПОНЕДЕЛЬНИК",
    "ВТОРНИК",
    "СРЕДА",
    "ЧЕТВЕРГ",
    "ПЯТНИЦА",
    "СУББОТА",
    "ВОСКРЕСЕНЬЕ"
]
# Добавил суперкрутой комментарий - тут расписание пишется!
schedule = [
    # НЕДЕЛЯ 1
    [
        [
            {"time": "3-4", "subject": "ФИЗИЧЕСКАЯ КУЛЬУРА", "teacher": "Володина И.А.",
             "room": "УЛК 5"},
            {"time": "5-8", "subject": "РАСПРЕДЕЛИТЕЛЬНЫЙ КОНРОЛЬ ВЕРСИЙ КОДА", "teacher": "Сычев О.А.   Денисов",
             "room": "В 902-а"}
        ],
        [
            {"time": "5-8", "subject": "ООП", "teacher": "Литовкин Д.В.",
             "room": "В 902-а"}
        ],
        [],
        [],
        [],
        [],
        []
    ],
    [
        [], [], [], [], [], [], []
    ]
]

#ЕЩЕ ДВА КОММЕНТАРИЯ СЮДЫ
#АПЬВЛЛВЬЫВАЛОАЛЫ
#Добавлю еще сюда коммент ЯЯЯЯЯЯЯЯЯ ТУУУУУУТ  а еще я в расписание добавил
def get_schedule(week, day):
    # Проверка корректности ввода
    if week not in [1, 2]:
	# проверка на неделю
        print("Ошибка: неделя должна быть либо 1 либо 2. Цифрами")
        return

    if day not in range(1, 8):
        print("Ошибка: день должен быть от 1 до 7")
        return

    # Получаем расписание на этот день
    day_schedule = schedule[ week - 1][day - 1]

    # Вывод
    print("\n" + "=" * 60)
    print(f"РАСПИСАНИЕ ДЛЯ ГРУППЫ ПРИН-366")
    print(f"Неделя {week}, {days_of_week[day - 1]}")
    print("=" * 60)

    if not day_schedule:
        print("Отдыхаем")
    else:
        for lesson in day_schedule:
            print(f"\n {lesson['time']} пара")
            print(f"{lesson['subject']}")
            if lesson['teacher']:
                print(f" {lesson['teacher']}")
            if lesson['room']:
                print(f"{lesson['room']}")
            print("-" * 40)

#тут тоже будет комментарий топовый
while True:
    print("\n" + "=" * 60)
    # Добавлено
    print("Пожалуйста введите номер недели (1-первая или 2-вторая) и номер дня (1-7)")
    print("Или '0' для выхода из программы")

    try:
        week = int(input("Неделя: "))
        if week == 0:
            print("Пока")
            break

        day = int(input("День (1-пн, 7-вс): "))

        get_schedule(week, day)

    except ValueError:
        print("Ошибка: введите числа!")