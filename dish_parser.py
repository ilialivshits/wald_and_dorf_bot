def dish_parser(message_from_chief):
    # ВХОД: список блюд, отправленный боту завпитами (message_from_chief).
    # ВЫХОД: словарь, состоящий из пар "название блюда - количества блюда" (to_cook)
    #        + множество повторяющихся блюд (repeated_dishes)

    # Оформление списка:
    # Количество блюд указывается через пробел после названия.
    # Если блюдо одно, то количество не указывается.
    # Каждое новое блюдо начинается с новой строки.
    # Например,
    #       "Борщ 4
    #       Макароны 3
    #       Сырный суп 2".

    # Разделяем сообщение на список из строк и преобразовываем всё к нижнему регистру.
    message_from_chief = message_from_chief.lower()
    message_from_chief_divided = message_from_chief.split('\n')

    to_cook = dict()
    repeated_dishes = set()

    # Функция добавления блюда в to_cook
    def add_dish(name, count):
        if name == '':
            # Если название блюда оказывается пустым, то ничего не делаем
            pass
        elif name in to_cook:
            # Если такое блюдо уже было,
            # То мы сообщим об этом завпитам
            # Добавим его в список повторяющихся блюд
            repeated_dishes.add(name)
            # И прибавим новое количество к уже имеющемуся в to_cook
            to_cook[name] += count
        else:
            # Если всё хорошо,
            # То просто добавляем
            to_cook[name] = count

    # Перебираем строки в сообщении завпита
    for string in message_from_chief_divided:
        # Очищаем строку от пробелов в начале и в конце
        string = string.strip()
        # string_divided - строка, разбитая на слова
        string_divided = string.split()

        if string_divided == []:
            # Если строка была пустой, то он пропускает её
            pass
        elif string_divided[-1].isdigit():
            # Если последнее слово в ней является числом
            # Мы удаляем его и записываем в отдельную переменную
            dish_count = int(string_divided.pop())
            # А всё остальное, т. е. название блюда - в другую переменную
            dish_name = ' '.join(string_divided)
            # Добавляем блюдо в словарь
            add_dish(dish_name, dish_count)
        else:
            # Если же нет,
            # то добавляем всю строку, которая является названием блюда, и количество - 1
            add_dish(string, 1)

    return to_cook, repeated_dishes