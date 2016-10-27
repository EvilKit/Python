#Генератор персонажей

choise_1 = None
while choise_1 != "0":
    print(
    """
        \tОпции:
        \t0 - выход
        \t1 - создать персонажа
    """)

    choise_1 = input("Ваш выбор: ")
    if choise_1 == "0":
        print("До встречи!")
    elif choise_1 == "1":
        scores = 30
        while scores != 0:
            print(
            """
        \tХарактеристики:
        \t0 - Сила
        \t1 - Здоровье
        \t2 - Интеллект
        \t3 - Выйти
            """)
            choise_2 = input("Ваш выбор: ")
            character = {}
            if choise_2 == "3":
                scores = 0

            elif choise_2 == "0":
                print("Вы выбрали силу")
                print("Какое кол-во очков вы хотите добавить?\n", "У вас сейчас есть", scores, "очков")
                force_s = int(input(": "))
                if force_s < 0 or force_s > scores:
                    print("Недопустимое значение")
                    force_s = 0
                scores -= force_s
                character["сила"] = force_s
                print("У вас осталось", scores, "очков")

            elif choise_2 == "1":
                print("Вы выбрали здоровье")
                print("Какое кол-во очков вы хотите добавить?\n", "У вас сейчас есть", scores, "очков")
                health_s = int(input(": "))
                if health_s < 0 or health_s > scores:
                    print("Недопустимое значение")
                    health_s = 0
                scores -= health_s
                character["здоровье"] = health_s
                print("У вас осталось", scores, "очков")

            elif choise_2 == "2":
                print("Вы выбрали интеллект")
                print("Какое кол-во очков вы хотите добавить?\n", "У вас сейчас есть", scores, "очков")
                brains_s = int(input(": "))
                if brains_s < 0 or brains_s > scores:
                    print("Недопустимое значение")
                    brains_s = 0
                scores -= brains_s
                character["интеллект"] = brains_s
                print("У вас осталось", scores, "очков")
            else:
                print("Недопустимое значение")
        print("Как же его зовут?")
        name = input(": ")
        character["имя"] = name
        print("Ваш герой: \n")
        print(character)
