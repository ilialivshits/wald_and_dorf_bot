def first_blank_row_finder(table, biggest_column):
    # Вход: таблица Excel (table), самый длинный столбец в ней (biggest_column)
    # Выход: первая пустая строка (first_blank_row)
    value = True
    first_blank_row = 0
    while value != None:
        # Пробегаемся по всем ячейкам столбца до тех пор, пока какая-то из них не окажется пустой
        # Записываем её строку, как первую пустую
        value = table.cell(row=first_blank_row + 1, column=biggest_column).value
        first_blank_row += 1
    return first_blank_row